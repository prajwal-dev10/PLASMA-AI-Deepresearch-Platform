from dotenv import load_dotenv
import os
os.environ["OPENAI_AGENTS_DISABLE_TRACING"] = "1"

from openai import AsyncOpenAI
from agents import set_default_openai_client

load_dotenv(override=True)

client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(client)