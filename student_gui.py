import tkinter as tk
from tkinter import messagebox

FILE = "students.txt"


# ---------- Generate Student ID ----------
def generate_id():
    try:
        with open(FILE, "r") as f:
            lines = f.readlines()

            if len(lines) == 0:
                return 101

            last_id = int(lines[-1].split(",")[0])
            return last_id + 1

    except FileNotFoundError:
        return 101


# ---------- Add Student ----------
def add_student():

    sid = generate_id()
    name = name_entry.get()
    age = age_entry.get()
    dept = dept_entry.get()

    if name == "" or age == "" or dept == "":
        messagebox.showwarning("Warning", "All fields required")
        return

    with open(FILE, "a") as f:
        f.write(f"{sid},{name},{age},{dept}\n")

    messagebox.showinfo("Success", f"Student Added (ID: {sid})")

    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)


# ---------- View Students ----------
def view_students():

    listbox.delete(0, tk.END)

    try:
        with open(FILE, "r") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())

    except FileNotFoundError:
        pass


# ---------- Search Student ----------
def search_student():

    sid = id_entry.get()

    listbox.delete(0, tk.END)

    found = False

    try:
        with open(FILE, "r") as f:
            for line in f:
                if line.startswith(sid + ","):
                    listbox.insert(tk.END, line.strip())
                    found = True

        if not found:
            messagebox.showinfo("Result", "Student not found")

    except FileNotFoundError:
        pass


# ---------- Delete Student ----------
def delete_student():

    sid = id_entry.get()

    lines = []
    deleted = False

    try:
        with open(FILE, "r") as f:
            lines = f.readlines()

        with open(FILE, "w") as f:
            for line in lines:

                if not line.startswith(sid + ","):
                    f.write(line)
                else:
                    deleted = True

        if deleted:
            messagebox.showinfo("Success", "Student deleted")
        else:
            messagebox.showinfo("Result", "Student not found")

    except FileNotFoundError:
        pass


# ---------- Update Student ----------
def update_student():

    sid = id_entry.get()

    lines = []
    updated = False

    try:
        with open(FILE, "r") as f:
            lines = f.readlines()

        with open(FILE, "w") as f:
            for line in lines:

                student_id, name, age, dept = line.strip().split(",")

                if student_id == sid:

                    name = name_entry.get()
                    age = age_entry.get()
                    dept = dept_entry.get()

                    updated = True

                f.write(f"{student_id},{name},{age},{dept}\n")

        if updated:
            messagebox.showinfo("Success", "Student Updated")
        else:
            messagebox.showinfo("Result", "Student not found")

    except FileNotFoundError:
        pass


# ---------- GUI WINDOW ----------
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x500")


# ---------- Labels ----------
tk.Label(root, text="Student ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Department").pack()
dept_entry = tk.Entry(root)
dept_entry.pack()


# ---------- Buttons ----------
tk.Button(root, text="Add Student", width=20, command=add_student).pack(pady=5)

tk.Button(root, text="View Students", width=20, command=view_students).pack(pady=5)

tk.Button(root, text="Search Student", width=20, command=search_student).pack(pady=5)

tk.Button(root, text="Update Student", width=20, command=update_student).pack(pady=5)

tk.Button(root, text="Delete Student", width=20, command=delete_student).pack(pady=5)


# ---------- Listbox ----------
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)


# ---------- Run GUI ----------
root.mainloop()