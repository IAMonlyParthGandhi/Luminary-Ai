"""SWOT analysis for the first 3 companies via Groq (llama-3.3-70b-versatile)."""
from app.core.groq import getClient, parseJson


def companiesAnalysis(company_info, api_key: str | None = None):
    """Return SWOT (strengths/weaknesses/opportunities/threats) for the first 3 companies."""
    client = getClient(api_key)

    prompt = f"""
    From the {company_info} find all the companies.

    Provide the following details for each companies:
    1. Official Name
    2. Strengths of Company
    3. Weakness of Company
    4. Opportunity of Company
    5. Threats to the Company

    Strictly always return response in JSON format as shown in example.
    Compulsarily, find all the details of only first 3 companies.
    """

    prompt += """
    Example:
    Output:
    {
        "companies": [
            {
                "Official Name": "Challengerate",
                "Strengths of Company": "Strong e-commerce platform, diverse range of products, strategic location in Surat, India",
                "Weakness of Company": "Limited geographical presence, lack of website, intense competition in the retail industry",
                "Opportunity of Company": "Expansion into new markets, increasing demand for online shopping, potential partnerships with suppliers",
                "Threats to the Company": "Intense competition from established players, changing consumer preferences, economic downturn"
            },
            {
                "Official Name": "Reliance Retail",
                "Strengths of Company": "Strong brand reputation, wide range of products, extensive geographical presence",
                "Weakness of Company": "High operating costs, dependence on few suppliers, intense competition in the retail industry",
                "Opportunity of Company": "Expansion into new markets, increasing demand for online shopping, potential partnerships with international brands",
                "Threats to the Company": "Intense competition from e-commerce players, changing consumer preferences, regulatory challenges"
            },
            {
                "Official Name": "V-Mart Retail",
                "Strengths of Company": "Strong presence in Tier 2 and Tier 3 cities, diverse range of products, efficient supply chain management",
                "Weakness of Company": "Limited presence in metro cities, high dependence on few suppliers, intense competition in the retail industry",
                "Opportunity of Company": "Expansion into new markets, increasing demand for online shopping, potential partnerships with local suppliers",
                "Threats to the Company": "Intense competition from established players, changing consumer preferences, economic downturn"
            }
        ]
    }
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
