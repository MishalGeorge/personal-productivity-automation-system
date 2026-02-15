import sqlite3
from datetime import datetime
DB_NAME = "app.db"

def add_task(data):
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    cursor.execute("""
                   INSERT INTO tasks(task_name, status, due_date)
                   VALUES(?,?,?)""",data)
    conn.commit()
    task_id = cursor.lastrowid
    log_task_addition(task_id, data[0])
    conn.close()
    return

def view_table():
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    cursor.execute("""SELECT * FROM tasks""")
    conn.commit()
    tasks_task = cursor.fetchall()
    conn.close()
    return tasks_task
    

def view_pending_tasks():
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    cursor.execute("""SELECT * FROM tasks WHERE status='pending'""")
    pending_tasks = cursor.fetchall()
    conn.commit()
    conn.close()
    return pending_tasks

def mark_task_completed(task_id):
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    cursor.execute("""UPDATE tasks SET status='completed' WHERE id=?""", (task_id,))
    conn.commit()
    conn.close()
    print("Task marked as completed.")
    return

def delete_task(delete_id):
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    
    cursor.execute("SELECT task_name FROM tasks WHERE id=?", (delete_id,))
    result = cursor.fetchone()
    if result:
        task_name = result[0]
        log_task_deletion(delete_id, task_name)
        cursor.execute("""DELETE FROM tasks WHERE id =?""", (delete_id,))
        conn.commit()
        conn.close()
        print("Task deleted successfully.")
    else:
        print("Task not found.")
    return

def log_task_addition(task_id, task_name):
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    log_message="ADDED TASK "+task_name+" WITH ID "+str(task_id)
    cursor.execute("""
                   INSERT INTO logs(log_type, message)
                   VALUES(?,?)""",("ADD_TASK", log_message))
    conn.commit()
    conn.close()
    return

def log_task_deletion(task_id, task_name):
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    log_message="DELETED TASK "+task_name+" WITH ID "+str(task_id)
    cursor.execute("""
                   INSERT INTO logs(log_type, message)
                   VALUES(?,?)""",("DELETE_TASK", log_message))
    conn.commit()
    conn.close()
    return

def summarize_tasks():
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    total_tasks=cursor.execute("""SELECT COUNT(*) FROM tasks""").fetchone()[0]
    pending_tasks=cursor.execute("""SELECT COUNT(*) FROM tasks WHERE status='pending'""").fetchone()[0]
    completed_tasks=cursor.execute("""SELECT COUNT(*) FROM tasks WHERE status='completed'""").fetchone()[0]
    conn.commit()
    conn.close()
    summary=f"Total Tasks: {total_tasks}, Pending Tasks: {pending_tasks}, Completed Tasks: {completed_tasks}"
    return summary



