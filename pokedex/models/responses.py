from typing import Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel, validator
from pydantic.generics import GenericModel

DataT = TypeVar('DataT')


class Error(BaseModel):
    code: str
    detail: Union[str, List]


class Response(GenericModel, Generic[DataT]):
    data: Optional[DataT]
    error: Optional[Error]

    @validator('error', always=True)
    def check_consistency(cls, v, values):
        if v is not None and values['data'] is not None:
            raise ValueError('must not provide both data and error')
        if v is None and values.get('data') is None:
            raise ValueError('must provide data or error')
        return v
