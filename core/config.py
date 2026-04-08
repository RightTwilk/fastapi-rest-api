from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):

    DATABASE_URL: str = Field(..., init=False)
    SECRET_KEY: str = Field(..., init=False)

    class Config:

        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()