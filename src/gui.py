import tkinter as tk
from tkinter import messagebox
from task_assigner import add_task, get_tasks, delete_task, mark_task_complete
from database import create_table
from tkcalendar import DateEntry

# Initialize the database
create_table()

# Function to add a task from the GUI
def add_task_gui():
    name = entry_name.get()
    desc = entry_desc.get()
    priority = priority_var.get()  # Get priority from dropdown
    due_date = entry_due_date.get()  # Get date from date picker

    if name and priority and due_date:  # Ensure mandatory fields are filled
        add_task(name, desc, priority, due_date)
        messagebox.showinfo("Success", f'Task "{name}" added!')
        refresh_task_list()
    else:
        messagebox.showerror("Error", "Please fill in all the mandatory fields.")

# Function to list all tasks in the GUI
def refresh_task_list():
    task_listbox.delete(0, tk.END)
    tasks = get_tasks()
    if tasks:
        for task in tasks:
            task_listbox.insert(tk.END, f"ID: {task[0]} | {task[1]} | {task[3]} | {task[4]} | {task[5]}")
    else:
        task_listbox.insert(tk.END, "No tasks found.")

# Function to delete a task
def delete_task_gui():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        task_id = selected_task.split('|')[0].replace('ID: ', '').strip()
        delete_task(int(task_id))
        messagebox.showinfo("Success", f'Task ID {task_id} deleted!')
        refresh_task_list()
    except:
        messagebox.showerror("Error", "Please select a task to delete.")

# Function to mark task as complete
def complete_task_gui():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        task_id = selected_task.split('|')[0].replace('ID: ', '').strip()
        mark_task_complete(int(task_id))
        messagebox.showinfo("Success", f'Task ID {task_id} marked as complete!')
        refresh_task_list()
    except:
        messagebox.showerror("Error", "Please select a task to mark as complete.")

# Set up the main window
root = tk.Tk()
root.title("Task Manager")

# Set a minimum window size (width x height)
root.minsize(500, 400)

# Add Task section
frame_add_task = tk.Frame(root)
frame_add_task.pack(pady=10, padx=10, fill=tk.X, expand=True)

lbl_name = tk.Label(frame_add_task, text="Task Name:")
lbl_name.grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_add_task)
entry_name.grid(row=0, column=1, padx=5, sticky="ew")

lbl_desc = tk.Label(frame_add_task, text="Description:")
lbl_desc.grid(row=1, column=0, sticky="w")
entry_desc = tk.Entry(frame_add_task)
entry_desc.grid(row=1, column=1, padx=5, sticky="ew")

# Dropdown menu for priority selection
lbl_priority = tk.Label(frame_add_task, text="Priority:")
lbl_priority.grid(row=2, column=0, sticky="w")
priority_var = tk.StringVar(value="Low")  # Default priority
priority_menu = tk.OptionMenu(frame_add_task, priority_var, "Low", "Medium", "High")
priority_menu.grid(row=2, column=1, padx=5, sticky="ew")

# Date picker for due date selection
lbl_due_date = tk.Label(frame_add_task, text="Due Date:")
lbl_due_date.grid(row=3, column=0, sticky="w")
entry_due_date = DateEntry(frame_add_task, date_pattern='yyyy-mm-dd')
entry_due_date.grid(row=3, column=1, padx=5, sticky="ew")

btn_add = tk.Button(frame_add_task, text="Add Task", command=add_task_gui)
btn_add.grid(row=4, column=1, pady=10, sticky="ew")

frame_add_task.columnconfigure(1, weight=1)

# Task list section
frame_task_list = tk.Frame(root)
frame_task_list.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

task_listbox = tk.Listbox(frame_task_list, width=60, height=10)
task_listbox.pack(fill=tk.BOTH, expand=True)

# Task actions (delete, complete)
frame_task_actions = tk.Frame(root)
frame_task_actions.pack(pady=10, padx=10)

btn_delete = tk.Button(frame_task_actions, text="Delete Task", command=delete_task_gui, width=15)
btn_delete.pack(side=tk.LEFT, padx=10)

btn_complete = tk.Button(frame_task_actions, text="Mark Task Complete", command=complete_task_gui, width=15)
btn_complete.pack(side=tk.LEFT, padx=10)

# Refresh button to update task list
btn_refresh = tk.Button(root, text="Refresh Task List", command=refresh_task_list)
btn_refresh.pack(pady=5)

# Initial task list load
refresh_task_list()

# Start the GUI loop
root.mainloop()
