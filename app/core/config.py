from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Grid Guard AI"
    version: str = "1.0.0"

    # Future use
    openai_api_key: str = ""

    class Config:
        env_file = ".env"

settings = Settings()