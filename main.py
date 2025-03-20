import sys
import os
import customtkinter as ctk

# Ensure database.py can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import add_task, get_tasks, delete_task, mark_as_done

# 🔹 Initialize CustomTkinter with dark mode
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# 🔹 Main App Class
class ToDoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window settings
        self.title("Modern To-Do List")
        self.geometry("500x600")
        self.resizable(False, False)

        # Title Label
        self.title_label = ctk.CTkLabel(self, text="✅ To-Do List", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        # Task Entry
        self.task_entry = ctk.CTkEntry(self, placeholder_text="Enter a task...", width=350)
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_button = ctk.CTkButton(self, text="Add Task", command=self.add_task, fg_color="#007BFF")
        self.add_button.pack(pady=10)

        # Task List Frame
        self.task_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.task_frame.pack(pady=10, fill="both", expand=True)

        # Load tasks from database
        self.load_tasks()

    def add_task(self):
        """Adds a new task and refreshes the UI."""
        task_text = self.task_entry.get()
        if task_text:
            add_task(task_text)
            self.task_entry.delete(0, "end")
            self.load_tasks()

    def load_tasks(self):
        """Loads all tasks and displays them in the UI."""
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        tasks = get_tasks()
        for task in tasks:
            task_id, task_text, status = task
            task_frame = ctk.CTkFrame(self.task_frame, fg_color="#222222", corner_radius=10)
            task_frame.pack(fill="x", pady=5, padx=10)

            # Task Checkbox
            check_var = ctk.BooleanVar(value=(status == "done"))
            checkbox = ctk.CTkCheckBox(task_frame, text=task_text, variable=check_var, command=lambda t=task_id: self.complete_task(t))
            checkbox.pack(side="left", padx=10)

            # Delete Button
            delete_button = ctk.CTkButton(task_frame, text="❌", width=40, fg_color="#FF4C4C",
                                          command=lambda t=task_id: self.delete_task(t))
            delete_button.pack(side="right", padx=5)

    def complete_task(self, task_id):
        """Marks a task as done and refreshes the UI."""
        mark_as_done(task_id)
        self.load_tasks()

    def delete_task(self, task_id):
        """Deletes a task and refreshes the UI."""
        delete_task(task_id)
        self.load_tasks()

# 🔹 Run the App
if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
