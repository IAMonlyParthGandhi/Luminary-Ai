"""Luminary AI backend — FastAPI entrypoint.

Run with:  uvicorn main:app --host 0.0.0.0 --port 8000 --reload   (from backend/)
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.chat import router as chat_router
from app.routers.company import router as company_router
from app.routers.seo import router as seo_router
from app.routers.taglines import router as taglines_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/home")
def readRoot():
    return {"message": "Hello World!", "team": ["Vatsal", "Miten", "Laskhit"]}


app.include_router(company_router)
app.include_router(chat_router)
app.include_router(taglines_router)
app.include_router(seo_router)
