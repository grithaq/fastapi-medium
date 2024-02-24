from pydantic_settings import BaseSettings
from starlette.config import Config


config_env = Config(".env")


class Settings(BaseSettings):
    API_V1_STR: str = config_env("API_V1_STR")
    PROJECT_NAME: str = config_env("PROJECT_NAME")
    PROJECT_VERSION: str = config_env("PROJECT_VERSION")
    DESCRIPTION: str = config_env("DESCRIPTION")
    DEBUG: str = config_env("DEBUG")


settings = Settings()