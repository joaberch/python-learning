import tkinter as tk
import task
from datetime import datetime
from tkcalendar import Calendar

date = datetime.now()

tasks = []

def validate_input(p):
    if p.isdigit() and 1 <= int(p) <= 9:
        return True
    elif p == "":
        return True
    return False

def get_date_selected():
    due_date = cal.get_date()
    date_label.config(text="Date : " + str(due_date))

def create_task():
    task_name = name.get()
    task_description = description.get()
    task_priority = priority.get()
    due_date = cal.get_date()
    new_task = task.task(due_date, task_name, task_description, task_priority)
    tasks.append(new_task)

    setup_tasks_user_ui()

def setup_tasks_user_ui():
    ui = tk.Toplevel()
    ui.title("Tasks")

    frame = tk.Frame(ui)
    frame.pack(pady=20)

    check_buttons = []
    for task in tasks:
        var = tk.BooleanVar
        check_button = tk.Checkbutton(frame, text=f"{task.name} - {task.due_date} - {task.priority} - {task.description}", variable=var)
        check_button.pack(anchor='w', pady=2)
        check_buttons.append((check_button, var))

    ui.mainloop()

def setup_tasks_manager_ui():
    global name, description, priority, cal, date_label
    tasks_manager = tk.Tk()
    tasks_manager.title("Task Manager")

    welcome = tk.Label(tasks_manager, text="Welcome to this task manager")
    welcome.pack(pady=10)

    name = tk.Entry(tasks_manager)
    name.insert(0, "Task Name")
    name.pack(pady=10)

    description = tk.Entry(tasks_manager)
    description.insert(0, "Description")
    description.pack(pady=10)
    vcmd = (tasks_manager.register(validate_input), '%P')

    priority = tk.Entry(tasks_manager, validate='key', validatecommand=vcmd)  # 'key' validation to trigger on keypress
    priority.insert(0, '1')  # Default value set to 1
    priority.pack(pady=10)

    date_label = tk.Label(tasks_manager, text="Select a date")
    date_label.pack(pady=20)
    cal = Calendar(tasks_manager, selectmode='day', year=date.year, month=date.month, day=date.day)
    cal.pack(pady=20)
    tk.Button(tasks_manager, text="Select Date", command=get_date_selected).pack(pady=20)

    button = tk.Button(tasks_manager, text="Add Task", command=create_task)
    button.pack(pady=10)

    setup_tasks_user_ui()
    tasks_manager.mainloop()

setup_tasks_manager_ui()
