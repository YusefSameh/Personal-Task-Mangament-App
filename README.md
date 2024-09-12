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
- Encapsulated as an executable using PyInstaller.

## Prerequisites
- Python 3.7 or higher
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/yourrepo.git
    cd yourrepo
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python gui.py
    ```

### Packaging the Application
To create an executable of the application (optional):

    ```bash
    pyinstaller --onefile --windowed --icon=app_icon.ico gui.py
    ```

This will generate an executable file in the `dist/` folder.

## Dependencies
- `tkinter`: For building the graphical user interface.
- `tkcalendar`: For the calendar and date entry widget.
- `pymysql`: For database interactions.
- `babel`: For date localization support.
- `pyinstaller`: To package the project into an executable (optional).

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
