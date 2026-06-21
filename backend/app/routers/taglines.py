"""Tagline / company-name generation endpoint."""
from fastapi import APIRouter
from pydantic import BaseModel

from app.config import GROQ_API_KEY
from app.services.taglines import generateTaglines

router = APIRouter()


class TaglineRequest(BaseModel):
    company_description: str
    company_sector: str


@router.post("/tagline-generator")
async def taglineGenerator(request: TaglineRequest):
    response = generateTaglines(request.company_description, request.company_sector, GROQ_API_KEY)
    return {"response": response}
