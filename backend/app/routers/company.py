"""Company research endpoints: profile lookup and SWOT analysis."""
from urllib.parse import unquote

from fastapi import APIRouter, HTTPException, Request

from app.config import GROQ_API_KEY
from app.services.analysis import companiesAnalysis
from app.services.company import getCompanyInfo

router = APIRouter()


@router.get("/company")
def getCompanyDetails(company: str, location: str):
    try:
        company = unquote(company)
        location = unquote(location)
        if GROQ_API_KEY is None:
            raise HTTPException(status_code=500, detail="API key is not set")
        return getCompanyInfo(company, location, api_key=GROQ_API_KEY)
    except Exception as e:
        return {"error": str(e)}


@router.post("/companies-analysis")
async def getCompaniesAnalysis(request: Request):
    try:
        company_info = await request.json()
        if GROQ_API_KEY is None:
            raise HTTPException(status_code=500, detail="API key is not set")
        return companiesAnalysis(company_info, api_key=GROQ_API_KEY)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
