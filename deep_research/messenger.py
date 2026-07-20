from dotenv import load_dotenv
import os
import requests
import resend

load_dotenv(override=True)

# ===============================
# Resend Configuration
# ===============================

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")      # Verified sender
EMAIL_TO = os.getenv("EMAIL_TO")                # Recipient

resend.api_key = RESEND_API_KEY


def send_email(subject, text_body, html_body):
    """
    Send an email using Resend.
    Function name intentionally unchanged.
    """

    if not RESEND_API_KEY:
        raise RuntimeError("RESEND_API_KEY is missing.")

    if not EMAIL_ADDRESS:
        raise RuntimeError("EMAIL_ADDRESS is missing.")

    if not EMAIL_TO:
        raise RuntimeError("EMAIL_TO is missing.")

    try:

        response = resend.Emails.send(
            {
                "from": EMAIL_ADDRESS,
                "to": [EMAIL_TO],
                "subject": subject,
                "text": text_body,
                "html": html_body,
            }
        )

        print("✅ Email sent successfully.")
        print(response)

        return response

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        raise


# ===============================
# Pushover
# ===============================

PUSHOVER_USER = os.getenv("PUSHOVER_USER")
PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")
PUSHOVER_URL = "https://api.pushover.net/1/messages.json"


def push(message):
    """
    Send a Pushover notification.
    Function name intentionally unchanged.
    """

    if not PUSHOVER_USER or not PUSHOVER_TOKEN:
        print("⚠️ Pushover is not configured.")
        return

    payload = {
        "user": PUSHOVER_USER,
        "token": PUSHOVER_TOKEN,
        "message": message,
    }

    try:

        response = requests.post(
            PUSHOVER_URL,
            data=payload,
            timeout=20,
        )

        if response.status_code == 200:
            print("✅ Push notification sent.")
        else:
            print(f"⚠️ Pushover Error: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"❌ Failed to send push notification: {e}")