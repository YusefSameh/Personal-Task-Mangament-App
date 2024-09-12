import argparse
from task_assigner import add_task, get_tasks, mark_task_complete, delete_task
from database import create_table

def main():
    create_table()  # Ensure table exists

    parser = argparse.ArgumentParser(description="Task Assigner")
    
    # Add a new task
    parser.add_argument('--add', nargs=4, metavar=('name', 'desc', 'priority', 'due_date'),
                        help='Add a new task')
    
    # List all tasks
    parser.add_argument('--list', action='store_true', help='List all tasks')
    
    # Mark task as complete
    parser.add_argument('--complete', type=int, metavar='task_id', help='Mark task as complete')
    
    # Delete task
    parser.add_argument('--delete', type=int, metavar='task_id', help='Delete a task')

    args = parser.parse_args()

    if args.add:
        name, desc, priority, due_date = args.add
        add_task(name, desc, priority, due_date)
        print(f'Task "{name}" added!')

    elif args.list:
        tasks = get_tasks()
        if tasks:
            for task in tasks:
                print(f"ID: {task[0]}, Name: {task[1]}, Desc: {task[2]}, Priority: {task[3]}, Due: {task[4]}, Status: {task[5]}")
        else:
            print("No tasks found.")

    elif args.complete:
        task_id = args.complete
        mark_task_complete(task_id)
        print(f'Task {task_id} marked as complete!')

    elif args.delete:
        task_id = args.delete
        delete_task(task_id)
        print(f'Task {task_id} deleted!')

if __name__ == "__main__":
    main()
