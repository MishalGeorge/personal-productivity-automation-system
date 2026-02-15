import sqlite3
from datetime import datetime, timedelta
from email_service import send_reminder_email

DB_NAME = "app.db"

def check_and_send_reminders():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, title, appointment_date, appointment_time, email
    FROM appointments
    WHERE reminder_sent = 0
    """)
    appointments = cursor.fetchall()

    now = datetime.now()
    for appointment in appointments:
        id, title, appointment_date, appointment_time, email = appointment
        
        appointment_datetime = datetime.strptime(f"{appointment_date} {appointment_time}", "%Y-%m-%d %H:%M")
        if appointment_datetime - timedelta(hours=1) <= now < appointment_datetime:
            send_reminder_email(
                to_email=email,
                subject="Appointment Reminder",
                message=f"Reminder: Your appointment '{title}' is in 1 hour."
            )

            cursor.execute("""
            UPDATE appointments
            SET reminder_sent = 1
            WHERE id = ?
            """, (id,))
            conn.commit()

            print(f"✔ Email sent automatically for appointment ID {id}")

    conn.close()
