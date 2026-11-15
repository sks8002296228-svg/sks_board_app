from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "SKS Master API"
    API_VERSION: str = "3.0"
    SECRET_API_KEY: str = "sks_super_secret_key_2026"
    DEBUG_MODE: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
