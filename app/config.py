from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@db/formulas"
    APP_NAME: str = "Math Formula API"
    DEBUG: bool = True

settings = Settings()
