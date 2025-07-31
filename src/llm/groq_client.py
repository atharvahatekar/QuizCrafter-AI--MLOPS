from langchain_groq import ChatGroq
from src.config.settings import settings

def get_groq_llm():
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model_name=settings.MODEL_NAME,
        temperature=settings.TEMPERATURE,
        max_retries=settings.MAX_RETRIES
    )
# This function initializes and returns a Groq LLM client with the specified settings.