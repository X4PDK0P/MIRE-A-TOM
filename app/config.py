from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/formulas"
    APP_NAME: str = "Math Formula API"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
