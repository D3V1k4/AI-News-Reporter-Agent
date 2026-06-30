import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import EMAIL, PASSWORD


def send_email(html):

    msg = MIMEMultipart("alternative")

    msg["Subject"] = "📰 Daily AI Pulse"

    msg["From"] = EMAIL

    msg["To"] = EMAIL        # send to yourself for now

    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

        smtp.starttls()

        smtp.login(EMAIL, PASSWORD)

        smtp.send_message(msg)

    print("✅ Newsletter sent successfully!")