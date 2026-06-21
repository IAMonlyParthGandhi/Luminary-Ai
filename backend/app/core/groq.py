"""Shared Groq client and JSON parsing helpers.

Replaces the Groq-client construction and the regex-strip + json.loads block that
was previously copy-pasted across company, analysis, taglines and seo services.
"""
import json
import re

from groq import Groq

from app.config import GROQ_API_KEY


def getClient(api_key: str | None = None) -> Groq:
    """Return a Groq client, defaulting to the configured key."""
    return Groq(api_key=api_key or GROQ_API_KEY)


def parseJson(content: str):
    """Strip ```json fences and parse the model's response into a dict.

    Raises ValueError on empty or malformed output (callers decide how to handle).
    """
    cleaned = re.sub(r"```json|```", "", content or "").strip()
    if not cleaned:
        raise ValueError("Empty response received from Groq AI.")
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        raise ValueError("Failed to parse response as JSON.") from e
