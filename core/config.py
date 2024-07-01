from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
import secrets

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v2"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = "cifarm-ai"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str = "cifarm-ai"
    OPENAI_API_KEY: str  # Ensure to set this in your .env file
    LANGCHAIN_API_KEY: str  # 새 필드 추가

    class Config:
        env_file = ".env"
