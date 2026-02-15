import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_ADDRESS, EMAIL_PASSWORD
from log import log_email_sent, log_email_failed
def send_reminder_email(to_email, subject, message):

    msg = MIMEMultipart()
    msg["From"] =EMAIL_ADDRESS 
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
    
        log_email_sent(to_email, subject)
        print("✅ Email sent successfully")

    except Exception as e:
        log_email_failed(to_email, subject)
        print("❌ Failed to send email:", e)
