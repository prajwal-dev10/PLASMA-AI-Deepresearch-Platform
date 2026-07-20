from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field
import json
import os

load_dotenv(override=True)

MODEL_NAME = os.getenv("DEFAULT_MODEL_NAME", "gemini-2.5-flash")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
HOW_MANY_SEARCHES = int(os.getenv("HOW_MANY_SEARCHES", "5"))

client = genai.Client(api_key=GEMINI_API_KEY)


class WebSearchItem(BaseModel):
    reason: str = Field(
        description="Why this search is useful."
    )

    query: str = Field(
        description="Search query."
    )


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(
        description="List of searches."
    )


INSTRUCTIONS = f"""
You are an expert research planner.

Given a research question,
produce EXACTLY {HOW_MANY_SEARCHES} web searches.

Each search should contain:

- reason
- query

Return ONLY valid JSON.

Example:

{{
    "searches": [
        {{
            "reason": "...",
            "query": "..."
        }}
    ]
}}
"""


class PlannerAgent:

    async def run(self, query: str) -> WebSearchPlan:

        prompt = f"""
{INSTRUCTIONS}

Research Question:

{query}
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        text = response.text.strip()

        # Remove markdown code fences if Gemini returns them
        text = text.replace("```json", "").replace("```", "").strip()

        try:
            data = json.loads(text)
            return WebSearchPlan.model_validate(data)

        except Exception as e:
            raise RuntimeError(
                f"PlannerAgent failed to parse JSON.\n\n{text}"
            ) from e


planner_agent = PlannerAgent()