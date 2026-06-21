"""SEO keyword endpoint."""
from fastapi import APIRouter

from app.services.seo import getSeo

router = APIRouter()


@router.get("/seo")
async def fetchSeo(company_description: str, location: str):
    """Fetch SEO keywords for a company."""
    return getSeo(company_description, location)
