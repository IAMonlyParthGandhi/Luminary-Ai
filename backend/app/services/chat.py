"""RAG chatbot service shared by the medical and marketing bots.

The two bots are identical apart from which Pinecone index they query, so a single
parameterized service backs both endpoints. Pipeline: HuggingFace embeddings ->
Pinecone similarity search (k=3) -> Groq (deepseek-r1-distill-llama-70b) -> strip
<think> reasoning tags.
"""
import re

from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from app.config import GROQ_API_KEY
from app.core.embeddings import downloadHuggingFaceEmbeddings
from app.core.prompts import CHATBOT_SYSTEM_PROMPT

# Maps a bot domain to its Pinecone index.
INDEXES = {"medical": "chatbot1", "marketing": "chatbot2"}


def _answer(msg: str, index_name: str) -> str:
    embeddings = downloadHuggingFaceEmbeddings()
    docsearch = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embeddings,
    )
    retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    llm = ChatGroq(api_key=GROQ_API_KEY, model_name="deepseek-r1-distill-llama-70b")
    prompt = ChatPromptTemplate.from_messages([
        ("system", CHATBOT_SYSTEM_PROMPT),
        ("human", "{input}"),
    ])

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    return rag_chain.invoke({"input": msg})["answer"]


async def getChatResponse(msg: str, domain: str) -> str:
    """Answer `msg` using the knowledge base for `domain` ('medical' or 'marketing')."""
    answer = str(_answer(msg, INDEXES[domain]))
    # Remove DeepSeek <think>...</think> reasoning tokens.
    return re.sub(r"<think>.*?</think>\s*", "", answer, flags=re.DOTALL)
