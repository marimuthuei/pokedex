from pydantic import BaseModel


class Success(BaseModel):
    total: int


class Contents(BaseModel):
    translated: str
    text: str
    translation: str


class TranslationResponse(BaseModel):
    success: Success
    contents: Contents
