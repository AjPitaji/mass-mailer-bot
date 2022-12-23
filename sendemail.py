import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv  

PORT = 587  
EMAIL_SERVER = "smtp.gmail.com" 


current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)


sender_email = os.getenv("email")
password_email = os.getenv("password")


def send_email(subject, receiver_email, name):
   
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("TedxSrmist", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
    <html>
      <body>
        <p>Hi participant,</p>
        <p>this is the invite letter</p>
        <p>https://drive.google.com/file/d/1ARAdueHDURamKdipGHLB5gd3mtBEvbeE/view?usp=sharing</p>
        <p>Best regards</p>
        <p>YOUR NAME</p>
      </body>
    </html>
    """,
        subtype="html",
    )


    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    send_email(
        subject="Invoice Reminder",
        name="Anuj",
        receiver_email="aj03jha@gmail.com",
    )