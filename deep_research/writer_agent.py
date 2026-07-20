from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field
import json
import os

load_dotenv(override=True)

MODEL_NAME = os.getenv("DEFAULT_MODEL_NAME", "gemini-2.5-flash")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


class ReportData(BaseModel):
    short_summary: str = Field(
        description="A short summary of the findings."
    )

    markdown_report: str = Field(
        description="Complete markdown report."
    )

    follow_up_questions: list[str] = Field(
        description="Topics worth researching next."
    )


INSTRUCTIONS = """
You are a senior AI research analyst.

You will receive:

1. The original research question.
2. A collection of summarized search results.

Your task:

• Write a professional research report.
• Use Markdown.
• Include headings and subheadings.
• Use bullet lists where appropriate.
• Include a conclusion.
• Be factual.
• Be detailed.
• Produce at least 1000 words.

Return ONLY valid JSON.

Example:

{
  "short_summary":"...",
  "markdown_report":"...",
  "follow_up_questions":[
      "...",
      "...",
      "..."
  ]
}
"""


class WriterAgent:

    async def run(self, prompt: str) -> ReportData:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=f"{INSTRUCTIONS}\n\n{prompt}",
        )

        text = response.text.strip()

        # Remove markdown code fences if Gemini returns them
        text = text.replace("```json", "").replace("```", "").strip()

        try:

            data = json.loads(text)

            return ReportData.model_validate(data)

        except Exception as e:

            raise RuntimeError(
                f"""
WriterAgent returned invalid JSON.

Returned:

{text}
"""
            ) from e


writer_agent = WriterAgent()