import os
import sqlite3
import smtplib
from email.message import EmailMessage

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle

conn = sqlite3.connect("Student2.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, subject TEXT, marks INTEGER)")
conn.commit()

PASS_MARK = 35
REPORT_FILE = "student_report.pdf"


def add_student():
    for i in range(1, int(input("How many students do you want to add? ")) + 1):
        print(f"\nEnter Details of Student {i}")
        sid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        marks = {}
        for j in range(int(input("How many subjects? "))):
            sub = input(f"Subject {j + 1} Name: ")
            marks[sub] = int(input(f"Marks in {sub}: "))
        for subject, mark in marks.items():
            cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (sid, name, subject, mark))
        conn.commit()
    print("\nAll Students Added Successfully.\n")


def update_student():
    sid = int(input("Enter ID to update: "))
    cursor.execute("SELECT DISTINCT name FROM students WHERE id = ?", (sid,))
    row = cursor.fetchone()
    if not row:
        print("Student not found.\n")
        return
    new_name = input(f"New name (old: {row[0]}): ") or row[0]
    cursor.execute("UPDATE students SET name = ? WHERE id = ?", (new_name, sid))
    for subject, old_mark in cursor.execute("SELECT subject, marks FROM students WHERE id = ?", (sid,)).fetchall():
        new_mark = input(f"New marks for {subject} (old: {old_mark}): ")
        if new_mark:
            cursor.execute("UPDATE students SET marks = ? WHERE id = ? AND subject = ?", (int(new_mark), sid, subject))
    conn.commit()
    print("Student updated.\n")


def print_rows(rows, empty_msg="No Records Found.\n"):
    if not rows:
        print(empty_msg)
        return False
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Subject: {row[2]} | Marks: {row[3]}")
    print()
    return True


def read_view():
    print_rows(cursor.execute("SELECT * FROM students").fetchall(), "No Records Found.\n")


def search_student():
    print("\nSearch By\n1. ID\n2. Name\n3. Marks")
    choice = input("Enter choice: ")
    if choice == "1":
        rows = cursor.execute("SELECT * FROM students WHERE id = ?", (int(input("Enter ID: ")),)).fetchall()
    elif choice == "2":
        rows = cursor.execute("SELECT * FROM students WHERE LOWER(name) = LOWER(?)", (input("Enter Name: "),)).fetchall()
    elif choice == "3":
        rows = cursor.execute("SELECT * FROM students WHERE marks = ?", (int(input("Enter Marks: ")),)).fetchall()
    else:
        print("Invalid Choice")
        return
    print_rows(rows, "Student Not Found")


def delete_student():
    choice = input("Delete (1) by ID or (2) All? ")
    if choice == "2":
        cursor.execute("DELETE FROM students")
        conn.commit()
        print("All records deleted.\n")
    elif choice == "1":
        sid = int(input("Enter ID to delete: "))
        if cursor.execute("SELECT id FROM students WHERE id = ?", (sid,)).fetchone():
            cursor.execute("DELETE FROM students WHERE id = ?", (sid,))
            conn.commit()
            print("Student deleted.\n")
        else:
            print("Student not found.\n")
    else:
        print("Invalid choice.\n")


def view_result():
    sid = int(input("Enter ID to view result: "))
    rows = cursor.execute("SELECT name, subject, marks FROM students WHERE id = ?", (sid,)).fetchall()
    if not rows:
        print("Student not found.\n")
        return
    name = rows[0][0]
    total = sum(row[2] for row in rows)
    result = "Pass" if all(row[2] >= PASS_MARK for row in rows) else "Fail"
    marks_str = ", ".join(f"{row[1]}: {row[2]}" for row in rows)
    print(f"ID: {sid} | Name: {name} | Subjects: {marks_str} | Total: {total} | Result: {result}\n")


def _group_students():
    rows = cursor.execute("SELECT id, name, subject, marks FROM students").fetchall()
    students = {}
    for sid, name, subject, mark in rows:
        students.setdefault(sid, {"id": sid, "name": name, "marks": {}})["marks"][subject] = mark
    return students


def reports():
    students = _group_students()
    if not students:
        print("No Records Found")
        return
    print("\n1. Total Report\n2. Pass Students\n3. Fail Students")
    choice = input("Enter Choice: ")
    if choice == "1":
        passed = sum(1 for s in students.values() if all(m >= PASS_MARK for m in s["marks"].values()))
        print("\nTotal Students:", len(students))
        print("Pass :", passed)
        print("Fail :", len(students) - passed)
    elif choice == "2":
        print("\nPass Students")
        for s in students.values():
            if all(m >= PASS_MARK for m in s["marks"].values()):
                print(f"ID: {s['id']} | Name: {s['name']} | Marks: {s['marks']}")
    elif choice == "3":
        print("\nFail Students")
        for s in students.values():
            if not all(m >= PASS_MARK for m in s["marks"].values()):
                print(f"ID: {s['id']} | Name: {s['name']} | Marks: {s['marks']}")
    else:
        print("Invalid Choice")


def download_report():
    students = _group_students()
    if not students:
        print("No records found.\n")
        return
    pdf = SimpleDocTemplate(REPORT_FILE)
    elements = [Paragraph("<b><font size=18>Student Management System Report</font></b>", getSampleStyleSheet()["Title"])]
    data = [["ID", "Name", "Marks", "Total", "Result"]]
    for s in students.values():
        total = sum(s["marks"].values())
        result = "Pass" if all(m >= PASS_MARK for m in s["marks"].values()) else "Fail"
        marks = ", ".join(f"{subject}: {mark}" for subject, mark in s["marks"].items())
        data.append([s["id"], s["name"], marks, total, result])
    table = Table(data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ]))
    elements.append(table)
    pdf.build(elements)
    print(f"\nPDF Report saved successfully as '{REPORT_FILE}'\n")


def email_file(file_path):
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.\n")
        return
    sender = input("Your Gmail address: ")
    app_password = input("Your Gmail App Password: ")
    receiver = input("Send to (recipient email): ")
    msg = EmailMessage()
    msg["Subject"] = f"Sending file: {os.path.basename(file_path)}"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Hi,\n\nPlease find the attached file.\n\nRegards.")
    ext = os.path.splitext(file_path)[1].lower()
    maintype, subtype = ("application", "octet-stream")
    if ext == ".csv":
        maintype, subtype = ("text", "csv")
    elif ext == ".db":
        maintype, subtype = ("application", "x-sqlite3")
    elif ext == ".pdf":
        maintype, subtype = ("application", "pdf")
    with open(file_path, "rb") as f:
        msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=os.path.basename(file_path))
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, app_password)
            smtp.send_message(msg)
        print(f"File emailed successfully to {receiver}.\n")
    except Exception as e:
        print(f"Failed to send email: {e}\n")


def email_report():
    if not cursor.execute("SELECT id FROM students LIMIT 1").fetchone():
        print("No records found. Add students first.\n")
        return
    download_report()
    email_file(REPORT_FILE)


def menu():
    while True:
        print("\n---Student Management System---\n1. Add\n2. Update\n3. Read/View\n4. Search\n5. Delete\n6. View Result\n7. Reports\n8. Download Report (pdf)\n9. Email Report\n10. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            read_view()
        elif choice == "4":
            search_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            view_result()
        elif choice == "7":
            reports()
        elif choice == "8":
            download_report()
        elif choice == "9":
            email_report()
        elif choice == "10":
            print("Exiting Student Management System")
            conn.close()
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    menu()
