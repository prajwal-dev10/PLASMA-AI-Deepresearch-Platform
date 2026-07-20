from dotenv import load_dotenv
from google import genai
import os

from messenger import send_email, push

load_dotenv(override=True)

MODEL_NAME = os.getenv("DEFAULT_MODEL_NAME", "gemini-2.5-flash")
USE_EMAIL = os.getenv("USE_EMAIL", "true").lower() == "true"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

INSTRUCTIONS = """
You are an Email Agent.

You will receive a complete research report in Markdown.

Your job is to:

1. Create a professional email subject.
2. Convert the report into clean HTML.
3. Generate a plain text version.
4. Send the email.

Return only:
SUBJECT:
TEXT:
HTML:
"""


class EmailAgent:

    async def run(self, markdown_report: str):

        prompt = f"""
{INSTRUCTIONS}

REPORT

{markdown_report}
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        content = response.text.strip()

        subject = "Deep Research Report"
        text_body = markdown_report
        html_body = f"<pre>{markdown_report}</pre>"

        try:
            if "SUBJECT:" in content:
                parts = content.split("HTML:")

                before_html = parts[0]
                html_body = parts[1].strip() if len(parts) > 1 else html_body

                subject = before_html.split("SUBJECT:")[1].split("TEXT:")[0].strip()

                text_body = before_html.split("TEXT:")[1].strip()

        except Exception:
            pass

        if USE_EMAIL:
            send_email(subject, text_body, html_body)
        else:
            push(f"{subject}\n\n{text_body}")

        return {
            "subject": subject,
            "text": text_body,
            "html": html_body,
        }


email_agent = EmailAgent()