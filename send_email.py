import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

# Change this to the email where you want to receive the test
RECEIVER = "your_other_email@gmail.com"

msg = EmailMessage()
msg["Subject"] = "Python Gmail SMTP Test"
msg["From"] = EMAIL
msg["To"] = RECEIVER

msg.set_content("""
Hello!

This is a test email sent successfully using Gmail SMTP and Python.

Regards,
AI News Reporter
""")

try:
    print("Connecting to Gmail...")

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)

    print("✅ Email sent successfully!")

except Exception as e:
    print("❌ Error:")
    print(e)