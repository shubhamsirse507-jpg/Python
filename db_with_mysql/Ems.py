import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime
import reportlab

# ---------- Database connection ----------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shubham@1978",
    database="Link_code2"
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS emp (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(20),
        sal DECIMAL(10,2),
        Ex INT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INT AUTO_INCREMENT PRIMARY KEY,
        emp_id INT,
        check_in DATETIME,
        check_out DATETIME,
        FOREIGN KEY (emp_id) REFERENCES emp(id) ON DELETE CASCADE
    )
""")
conn.commit()


# ---------- Employee logic ----------
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM emp")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)


def insert_emp():
    name = name_var.get().strip()
    sal = sal_var.get().strip()
    ex = ex_var.get().strip()

    if not name or not sal or not ex:
        messagebox.showwarning("Missing Data", "Please fill in all fields.")
        return

    try:
        sal = float(sal)
        ex = int(ex)
    except ValueError:
        messagebox.showerror("Invalid Input", "Salary must be a number and Experience must be an integer.")
        return

    cursor.execute(
        "INSERT INTO emp (name, sal, Ex) VALUES (%s, %s, %s)",
        (name, sal, ex)
    )
    conn.commit()
    messagebox.showinfo("Success", "Employee inserted successfully.")
    clear_fields()
    refresh_table()


def delete_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a row to delete.")
        return

    emp_id = tree.item(selected[0])["values"][0]
    cursor.execute("DELETE FROM emp WHERE id=%s", (emp_id,))
    conn.commit()
    messagebox.showinfo("Deleted", f"Employee with ID {emp_id} deleted.")
    refresh_table()
    refresh_attendance()


def clear_fields():
    name_var.set("")
    sal_var.set("")
    ex_var.set("")


def get_selected_emp_id():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select an employee first.")
        return None
    return tree.item(selected[0])["values"][0]


# ---------- Attendance logic ----------
def refresh_attendance():
    for row in att_tree.get_children():
        att_tree.delete(row)
    cursor.execute("""
        SELECT attendance.id, emp.name, attendance.check_in, attendance.check_out
        FROM attendance
        JOIN emp ON emp.id = attendance.emp_id
        ORDER BY attendance.id DESC
    """)
    for row in cursor.fetchall():
        att_tree.insert("", tk.END, values=row)


def check_in():
    emp_id = get_selected_emp_id()
    if emp_id is None:
        return

    # Prevent duplicate open check-ins (checked in but not yet checked out)
    cursor.execute(
        "SELECT id FROM attendance WHERE emp_id=%s AND check_out IS NULL",
        (emp_id,)
    )
    if cursor.fetchone():
        messagebox.showwarning("Already Checked In", "This employee already has an open check-in.")
        return

    now = datetime.now()
    cursor.execute(
        "INSERT INTO attendance (emp_id, check_in) VALUES (%s, %s)",
        (emp_id, now)
    )
    conn.commit()
    messagebox.showinfo("Checked In", f"Checked in at {now.strftime('%Y-%m-%d %H:%M:%S')}")
    refresh_attendance()


def check_out():
    emp_id = get_selected_emp_id()
    if emp_id is None:
        return

    cursor.execute(
        "SELECT id FROM attendance WHERE emp_id=%s AND check_out IS NULL ORDER BY id DESC LIMIT 1",
        (emp_id,)
    )
    row = cursor.fetchone()
    if not row:
        messagebox.showwarning("Not Checked In", "This employee has no open check-in to close.")
        return

    now = datetime.now()
    cursor.execute(
        "UPDATE attendance SET check_out=%s WHERE id=%s",
        (now, row[0])
    )
    conn.commit()
    messagebox.showinfo("Checked Out", f"Checked out at {now.strftime('%Y-%m-%d %H:%M:%S')}")
    refresh_attendance()


def on_close():
    cursor.close()
    conn.close()
    root.destroy()


# ---------- Build the GUI ----------
root = tk.Tk()
root.title("Employee Manager")
root.geometry("560x720")
root.resizable(False, False)

name_var = tk.StringVar()
sal_var = tk.StringVar()
ex_var = tk.StringVar()

form_frame = tk.Frame(root, padx=10, pady=10)
form_frame.pack(fill="x")

tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="w", pady=4)
tk.Entry(form_frame, textvariable=name_var).grid(row=0, column=1, pady=4)

tk.Label(form_frame, text="Salary:").grid(row=1, column=0, sticky="w", pady=4)
tk.Entry(form_frame, textvariable=sal_var).grid(row=1, column=1, pady=4)

tk.Label(form_frame, text="Experience:").grid(row=2, column=0, sticky="w", pady=4)
tk.Entry(form_frame, textvariable=ex_var).grid(row=2, column=1, pady=4)

btn_frame = tk.Frame(root, pady=5)
btn_frame.pack(fill="x")

tk.Button(btn_frame, text="Insert", width=12, command=insert_emp).pack(side="left", padx=10)
tk.Button(btn_frame, text="Delete Selected", width=14, command=delete_selected).pack(side="left", padx=10)
tk.Button(btn_frame, text="Refresh", width=12, command=refresh_table).pack(side="left", padx=10)

# ---------- Employee Table ----------
tk.Label(root, text="Employees", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10)

columns = ("id", "name", "sal", "ex")
tree = ttk.Treeview(root, columns=columns, show="headings", height=8)
tree.heading("id", text="ID")
tree.heading("name", text="Name")
tree.heading("sal", text="Salary")
tree.heading("ex", text="Experience")

tree.column("id", width=50, anchor="center")
tree.column("name", width=150, anchor="center")
tree.column("sal", width=100, anchor="center")
tree.column("ex", width=100, anchor="center")

tree.pack(fill="both", expand=False, padx=10, pady=5)

# ---------- Attendance Section ----------
tk.Label(root, text="Attendance (select an employee above, then Check In / Check Out)",
         font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10, pady=(15, 0))

att_btn_frame = tk.Frame(root, pady=5)
att_btn_frame.pack(fill="x")

tk.Button(att_btn_frame, text="Check In", width=12, bg="#d4f4dd", command=check_in).pack(side="left", padx=10)
tk.Button(att_btn_frame, text="Check Out", width=12, bg="#f4d4d4", command=check_out).pack(side="left", padx=10)
tk.Button(att_btn_frame, text="Refresh Log", width=12, command=refresh_attendance).pack(side="left", padx=10)

att_columns = ("id", "name", "check_in", "check_out")
att_tree = ttk.Treeview(root, columns=att_columns, show="headings", height=10)
att_tree.heading("id", text="Log ID")
att_tree.heading("name", text="Name")
att_tree.heading("check_in", text="Check In")
att_tree.heading("check_out", text="Check Out")

att_tree.column("id", width=60, anchor="center")
att_tree.column("name", width=120, anchor="center")
att_tree.column("check_in", width=170, anchor="center")
att_tree.column("check_out", width=170, anchor="center")

att_tree.pack(fill="both", expand=True, padx=10, pady=5)

refresh_table()
refresh_attendance()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()