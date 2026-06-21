"""SEO keyword generation via Groq (llama-3.3-70b-versatile).

Fetches a company profile, then extracts 10 SEO keywords per company.
"""
from app.config import GROQ_API_KEY
from app.core.groq import getClient, parseJson


def getCompanyInfo(company_name: str, location: str, api_key: str | None = None) -> str:
    """Return a raw company profile + 3 competitors (text, fed into getSeoInfo)."""
    client = getClient(api_key)

    prompt = f"""
    Company: {company_name}
    Location: {location}

    Provide the following details:
    1. Official Name
    2. Industry Type
    3. Headquarters / Main Office Location
    4. Key Products / Services
    5. Website (if available)

    Write the 3 competitiors based on the same location, sector and services

    Strictly always return response in JSON format as shown in example
    """

    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts structured company information."},
            {"role": "user", "content": prompt},
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        max_tokens=500,
    )

    return completion.choices[0].message.content


def getSeoInfo(company_info: str, api_key: str | None = None):
    """Extract 10 SEO keywords for the given company info."""
    client = getClient(api_key)

    prompt = f"""
    From the {company_info} the companies.

    Provide the following details for only the given company in input:
    1. 10 SEO Keywords
    Only give the the company name and SEO keywords
    Strictly always return response in JSON format as shown in example.
    Compulsarily find all the details for all the companies
    """

    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts structured company information."},
            {"role": "user", "content": prompt},
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        max_tokens=500,
    )

    return parseJson(str(completion.choices[0].message.content).strip())


def getSeo(company_description: str, location: str):
    company_info = getCompanyInfo(company_description, location, api_key=GROQ_API_KEY)
    return getSeoInfo(str(company_info), api_key=GROQ_API_KEY)
