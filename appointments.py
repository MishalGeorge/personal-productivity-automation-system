import sqlite3

DB_NAME = "app.db"


def add_appointment(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO appointments (title, description, appointment_date, appointment_time, email)
        VALUES (?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    log_appointments(cursor.execute("""SELECT last_insert_rowid()""").fetchone()[0], data[0])
    conn.close()
    return 

def view_appointments():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM appointments""")
    appointments = cursor.fetchall()
    conn.close()
    return appointments

def delete_appointment(delete_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM appointments WHERE id=?", (delete_id,))
    result = cursor.fetchone()
    if result:
        title = result[0]
        cursor.execute("DELETE FROM appointments WHERE id=?", (delete_id,))
        conn.commit()
        log_deletion(delete_id, title)
        print("Appointment deleted successfully.")
    else:
        print("Appointment not found")
    conn.close()
    return 

def log_appointments(appointment_id, title):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    log_message = "Added appointment " + title + " with ID " + str(appointment_id)
    cursor.execute("""
        INSERT INTO logs (log_type, message)
        VALUES (?, ?)""", ("ADD_APPOINTMENT", log_message))
    conn.commit()
    conn.close()
    return 

def log_deletion(appointment_id, title):
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    log_message="Deleted appointment " + title + " with ID " + str(appointment_id)
    cursor.execute("""INSERT INTO logs(log_type, message)
                   VALUES (?, ?)""",("DELETE_APPOINTMENT", log_message))
    conn.commit()
    conn.close()
    return 

def summarize_appointments():
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    Total_appointments=cursor.execute("""SELECT COUNT(*) FROM appointments""").fetchone()[0]
    Pending_appointments=cursor.execute("""SELECT  COUNT(*) FROM appointments WHERE reminder_sent=0""").fetchone()[0]
    Completed_appointments=cursor.execute("""SELECT  COUNT(*) FROM appointments WHERE reminder_sent=1""").fetchone()[0]
    conn.close()
    summary=f"Total Appointments: {Total_appointments}, Pending Appointments: {Pending_appointments}, Completed Appointments: {Completed_appointments}"
    return summary
    
