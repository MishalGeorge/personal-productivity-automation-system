from database import init_db
from appointments import add_appointment,view_appointments,delete_appointment,summarize_appointments
from time_reminder import check_and_send_reminders
from tasks import add_task, view_table,summarize_tasks,mark_task_completed, delete_task,view_pending_tasks
from time import sleep
import log
init_db()
def menu():
    while True:
        print("\n----- Personal Assistant -----")
        print("1. Manage Appointment")
        print("2. Manage Tasks")
        print("3. Summarize Appointments and Tasks")
        print("4. View Logs")
        print("5. Run Auto Email Trigger Service")
        print("6. Exit")
        print("--------------------------------")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\n--- Manage Appointments ---")
            print("1. Add Appointment")
            print("2. View Appointments")
            print("3. Delete Appointment")
            print("-------------------------")
            appointment_choice = input("Enter your choice: ")
            if appointment_choice == '1':
                title = input("Enter appointment title: ")
                description = input("Enter appointment description: ")
                date = input("Enter appointment date (YYYY-MM-DD): ")
                time = input("Enter appointment time (HH:MM): ")
                email = input("Enter email for reminders: ")
                add_appointment((title, description, date, time, email))
                print("Appointment added successfully.")
            elif appointment_choice == '2':
                appointments = view_appointments()
                for appt in appointments:
                    print(appt)
            elif appointment_choice == '3':
                delete_id = input("Enter the ID of the appointment to delete: ")
                delete_appointment(delete_id)
        
        elif choice == '2':
            print("\n--- Manage Tasks ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("------------------")
            task_choice = input("Enter your choice: ")
            if task_choice == '1':
                task_name = input("Enter task name: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                add_task((task_name, 'pending', due_date))
                print("Task added successfully.")
            elif task_choice == '2':
                all_tasks = view_table()
                print("\n--- All Tasks ---")
                for task in all_tasks:
                    print(task)
                pending_tasks = view_pending_tasks()
                print("\n--- Pending Tasks ---")
                for task in pending_tasks:
                    print(task)
            elif task_choice == '3':
                task_id = input("Enter the ID of the task to mark as completed: ")
                mark_task_completed(task_id)
            elif task_choice == '4':
                delete_id = input("Enter the ID of the task to delete: ")
                delete_task(delete_id)
        
        elif choice == '3':
            print("\n--- Summary ---")
            print(summarize_appointments())
            print(summarize_tasks())
        
        elif choice == '4':
            print("\n--- Logs ---")
            logs=log.view_logs()
            for log_entry in logs:
                print(log_entry)
        
        elif choice == '5':
            print("⏰ Auto Email Trigger Service Started...")
            while True:
                check_and_send_reminders()
                sleep(60)   
        
        elif choice == '6':
            print("Program Ended Goodbye:)")
            break

if __name__ == "__main__":
    menu()

