import sqlite3
from datetime import datetime
DB_NAME = "app.db"

def view_logs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM logs""")
    logs = cursor.fetchall()
    conn.close()
    return logs

def log_email_sent(to_email, subject):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    log_message = f"Sent email to {to_email} with subject '{subject}'"
    cursor.execute("""INSERT INTO logs (log_type, message) VALUES (?, ?)""", ("EMAIL_SENT", log_message))
    conn.commit()
    conn.close()

def log_email_failed(to_email, subject):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    log_message = f"Failed to send email to {to_email} with subject '{subject}'"
    cursor.execute("""INSERT INTO logs (log_type, message) VALUES (?, ?)""", ("EMAIL_FAILED", log_message))
    conn.commit()
    conn.close()