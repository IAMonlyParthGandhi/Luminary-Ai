"""HuggingFace embedding model loader (sentence-transformers/all-MiniLM-L6-v2, 384-D)."""
from langchain.embeddings import HuggingFaceEmbeddings


def downloadHuggingFaceEmbeddings():
    """Load the local HuggingFace embedding model used by the RAG chatbots."""
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
