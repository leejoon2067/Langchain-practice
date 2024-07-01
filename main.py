
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.api_v2 import api_router as v1_router
from core.config import Settings
from middleware.log import LogMiddleware

# 환경 변수 로드
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Settings 클래스의 인스턴스를 생성합니다.
settings = Settings()

app = FastAPI(
    title=settings.PROJECT_NAME,  # 인스턴스의 속성에 접근합니다.
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
app.add_middleware(LogMiddleware)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Include routers
app.include_router(v1_router, prefix=settings.API_V1_STR)
