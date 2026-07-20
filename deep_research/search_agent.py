from dotenv import load_dotenv
from duckduckgo_search import DDGS
from google import genai
import os

load_dotenv(override=True)

MODEL_NAME = os.getenv("DEFAULT_MODEL_NAME", "gemini-2.5-flash")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


def web_search(query: str) -> str:
    """
    Search the web using DuckDuckGo.
    Function name intentionally unchanged.
    """

    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        if not results:
            return "No search results found."

        output = []

        for i, result in enumerate(results, start=1):
            output.append(
                f"""
Result {i}

Title:
{result.get("title", "")}

Snippet:
{result.get("body", "")}

URL:
{result.get("href", "")}
"""
            )

        return "\n".join(output)

    except Exception as e:
        return f"Search failed: {e}"


INSTRUCTIONS = """
You are an expert research assistant.

You will receive:

• A search term
• A reason for the search

First, use the supplied search results.

Then:

- summarize the findings
- combine similar information
- remove duplicate facts
- cite URLs when useful
- keep the summary below 300 words
- never invent information
- only summarize what appears in the search results
"""


class SearchAgent:

    async def run(self, prompt: str) -> str:
        """
        Execute one web search and summarize it with Gemini.
        """

        # Extract search query
        query = ""

        for line in prompt.splitlines():
            if line.lower().startswith("search term"):
                query = line.split(":", 1)[1].strip()
                break

        if not query:
            query = prompt

        search_results = web_search(query)

        final_prompt = f"""
{INSTRUCTIONS}

Search Request

{prompt}


Search Results

{search_results}
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=final_prompt,
        )

        return response.text.strip()


search_agent = SearchAgent()