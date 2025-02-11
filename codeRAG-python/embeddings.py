# some_embedding_library.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def get_embedding(text):
    response = openai.Embedding.create(
        input=text, model="text-embedding-ada-002"  # Or another appropriate model
    )
    return response["data"][0]["embedding"]


