import sqlite3

def create_table():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    priority TEXT,
                    due_date TEXT,
                    status TEXT DEFAULT 'incomplete'
                    )''')
    conn.commit()
    conn.close()
