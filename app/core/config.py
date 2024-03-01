from pydantic_settings import BaseSettings
from starlette.config import Config


config_env = Config(".env")


class Settings(BaseSettings):
    API_V1_STR: str = config_env("API_V1_STR")
    PROJECT_NAME: str = config_env("PROJECT_NAME")
    PROJECT_VERSION: str = config_env("PROJECT_VERSION")
    DESCRIPTION: str = config_env("DESCRIPTION")
    DEBUG: str = config_env("DEBUG")
    SECRET_KEY: str = config_env("SECRET_KEY")
    ALGORITHM: str = config_env("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTE: int = config_env("ACCESS_TOKEN_EXPIRE_MINUTE")


settings = Settings()