"""RAG chatbot endpoints (medical + marketing), both backed by one service."""
from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat import getChatResponse

router = APIRouter()


class ChatRequest(BaseModel):
    msg: str


@router.post("/medical-bot")
async def medicalBot(request: ChatRequest):
    return {"response": await getChatResponse(request.msg, "medical")}


@router.post("/marketing-bot")
async def marketingBot(request: ChatRequest):
    return {"response": await getChatResponse(request.msg, "marketing")}
