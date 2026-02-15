import os

APP_NAME = "Appointment Scheduler & Email Reminder Manager"

DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M"


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
