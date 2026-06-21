"""Company name + tagline generation via Groq (llama-3.3-70b-versatile)."""
from app.core.groq import getClient, parseJson


def generateTaglines(company_description: str, company_sector: str, api_key: str | None = None):
    """Return exactly 5 company name suggestions, each with a tagline."""
    client = getClient(api_key)

    prompt = f"""
    You are a specialized naming consultant for businesses. Create exactly 5 unique and memorable company names based on the following:

    INPUTS NEEDED:
    1. Company description: {company_description}
    2. Industry/sector: {company_sector}

    REQUIREMENTS:
    - Generate exactly 5 names
    - Each name should be maximum 2-3 words
    - Include a brief rationale (max 15 words) explaining each name
    - Names should be:
    * Memorable and distinct
    * Available as .com domains
    * Easy to pronounce
    * Reflective of company values
    * Relevant to industry

    ### Instructions:
    - Ensure the JSON response is well-formed and strictly follows valid JSON syntax.
    - **Do not include unbalanced curly braces `{{}}` inside any key or value.**
    - **Do not wrap JSON in triple backticks (` ``` `).**
    - If any data is unavailable, return "Not Available" instead of leaving fields empty.
    - Strictly always return response in JSON format as shown in example.

    OUTPUT FORMAT:
    Return response strictly in this JSON format:

    """
    prompt += """
    EXAMPLE:
    INPUT:
    {
    "company_description": "We are company selling competition analysis and AI-a-a-s company",
    "company_sector": "Artificial Intelligence"
    }

    OUTPUT:
    {
    "company_names": [
            {
                "name": "AIAlyze",
                "TagLine": "Analyzing AI with precision"
            },
            {
                "name": "Intellex",
                "TagLine": "Intelligent analysis solutions"
            },
            {
                "name": "CompeteAI",
                "TagLine": "Competitive edge through AI"
            },
            {
                "name": "PulseAI",
                "TagLine": "Pulsing with AI insights"
            },
            {
                "name": "Cerebro",
                "TagLine": "Brainpower for business"
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
