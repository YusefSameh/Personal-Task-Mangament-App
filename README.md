# Personal Task Management System

A Python-based task management system with a graphical user interface (GUI) built using `tkinter` and `tkcalendar`. This application allows users to add, delete, and mark tasks as complete while saving the data in an SQLite database.

## Features
- Add new tasks with a description, priority, and due date.
- List all tasks, including completed and pending tasks.
- Mark tasks as completed.
- Delete tasks.
- Task prioritization (Low, Medium, High) with a dropdown selection.
- GUI for easy interaction using `tkinter`.
- Uses `tkcalendar` for date selection.

## Prerequisites
- Python 3.7 or higher
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository to your local machine

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python gui.py
    ```

## Dependencies
- `tkinter`: For building the graphical user interface.
- `tkcalendar`: For the calendar and date entry widget.
- `pymysql`: For database interactions.
- `babel`: For date localization support.

## License
This project is licensed under the MIT License.
