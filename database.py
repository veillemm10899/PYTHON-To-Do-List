import sqlite3
import os

# 🔹 Ensure database file is in the correct directory
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todo.db")
conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

def create_table():
    """Creates a tasks table if it doesn't exist."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        )
    ''')
    conn.commit()

def add_task(task_name):
    """Adds a new task to the database."""
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task_name,))
    conn.commit()

def get_tasks():
    """Retrieves all tasks from the database."""
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

def delete_task(task_id):
    """Deletes a task from the database using its ID."""
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

def mark_as_done(task_id):
    """Updates the task status to 'done' in the database."""
    cursor.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (task_id,))
    conn.commit()

# 🔹 Ensure the table is created when this file runs
create_table()
