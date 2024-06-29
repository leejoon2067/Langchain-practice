from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes

import uvicorn
import os

from langchain_community.llms import ollama
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title = "Langchain server",
    version = "1.0",
    description = "A simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path = "/openai"
)

llm = ChatOpenAI(model = "gpt-3.5-turbo")

prompt1 = ChatPromptTemplate.from_template(
    "Write me a answer about {topic} with 100 words."
)

add_routes(
    app,
    prompt1|llm,
    path = "/topic_example"
)

if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port = 8000)


# fatstapi routes
# from app.api.api_v1.endpoints import generation

# api_router = APIRouter()
# api_router.include_router(generation.router, prefix="/generation", tags=["generation"])