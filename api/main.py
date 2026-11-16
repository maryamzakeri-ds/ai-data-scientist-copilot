from fastapi import FastAPI
from pydantic import BaseModel

from app.services.llm_service import ask_llm


app = FastAPI(
    title='AI Data Scientist Copilot'
)


@app.get("/")
def home():
    return {
        'message': 'AI Data Scientist is running'
    }


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
def chat(request: ChatRequest):
    answer = ask_llm(request.question)
    return {
        'answer': answer
    }