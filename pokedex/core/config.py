import logging
from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    api_v1_str = "/api/v1"
    project_name: str
    pokemon_url: AnyHttpUrl
    translation_url: AnyHttpUrl
    cors_origins: List[AnyHttpUrl] = []
    log_level = logging.DEBUG
    client_timeout: int = 30  # in seconds

    @validator("cors_origins", pre=True)
    def validate_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
