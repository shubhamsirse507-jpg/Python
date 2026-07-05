import sqlite3
import csv        # for set all Data in csv file format and make it Downloadable for Download option's on SMS
import smtplib    # smtplib is (Standard mail transfer protocol Lib) with the help of this we can able to access the mail like (Gmail, Outlook) like vendor's
from email.message import EmailMessage
import os         # it use to check file exist if file exist then get the file
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle  # all are pdf layout and formatting properties
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

conn = sqlite3.connect("Student2.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER,
    name TEXT,
    subject TEXT,
    marks INTEGER
)
""")
conn.commit()

PASS_MARK = 35
REPORT_FILE = "student_report.pdf"


# Insert Data to DB
def add_student():
    total = int(input("How many students do you want to add? "))

    for i in range(total):
        print(f"\nEnter Details of Student {i+1}")

        sid = int(input("Enter ID: "))
        name = input("Enter Name: ")

        marks = {}
        n = int(input("How many subjects? "))

        for j in range(n):
            sub = input(f"Subject {j+1} Name: ")
            mark = int(input(f"Marks in {sub}: "))
            marks[sub] = mark

        for subject, mark in marks.items():
            cursor.execute(
                "INSERT INTO students VALUES (?, ?, ?, ?)",
                (sid, name, subject, mark)
            )

        conn.commit()

    print("\nAll Students Added Successfully.\n")


# Update data in DB
def update_student():
    sid = int(input("Enter ID to update: "))

    cursor.execute("SELECT DISTINCT name FROM students WHERE id = ?", (sid,))
    row = cursor.fetchone()

    if not row:
        print("Student not found.\n")
        return

    old_name = row[0]
    new_name = input(f"New name (old: {old_name}): ") or old_name

    # Update name for all rows of this student
    cursor.execute("UPDATE students SET name = ? WHERE id = ?", (new_name, sid))

    # Update marks per subject
    cursor.execute("SELECT subject, marks FROM students WHERE id = ?", (sid,))
    subject_rows = cursor.fetchall()

    for subject, old_mark in subject_rows:
        new_mark = input(f"New marks for {subject} (old: {old_mark}): ")
        if new_mark:
            cursor.execute(
                "UPDATE students SET marks = ? WHERE id = ? AND subject = ?",
                (int(new_mark), sid, subject)
            )

    conn.commit()
    print("Student updated.\n")


# Read data from DB
def read_view():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if not rows:
        print("No Records Found.\n")
        return

    print("\nStudent Records")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Subject: {row[2]} | Marks: {row[3]}")
    print()


# Search student from DB
def search_student():
    print("\nSearch By")
    print("1. ID")
    print("2. Name")
    print("3. Marks")

    choice = input("Enter choice: ")

    # Search by ID
    if choice == "1":
        sid = int(input("Enter ID: "))
        cursor.execute("SELECT * FROM students WHERE id = ?", (sid,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f"ID: {row[0]} | Name: {row[1]} | Subject: {row[2]} | Marks: {row[3]}")
        else:
            print("Student Not Found")

    # Search by Name
    elif choice == "2":
        name = input("Enter Name: ")
        cursor.execute("SELECT * FROM students WHERE LOWER(name) = LOWER(?)", (name,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f"ID: {row[0]} | Name: {row[1]} | Subject: {row[2]} | Marks: {row[3]}")
        else:
            print("Student Not Found")

    # Search by Marks
    elif choice == "3":
        mark = int(input("Enter Marks: "))
        cursor.execute("SELECT * FROM students WHERE marks = ?", (mark,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f"ID: {row[0]} | Name: {row[1]} | Subject: {row[2]} | Marks: {row[3]}")
        else:
            print("Student Not Found")

    else:
        print("Invalid Choice")


# Delete student from DB
def delete_student():
    choice = input("Delete (1) by ID or (2) All? ")

    if choice == "2":
        cursor.execute("DELETE FROM students")
        conn.commit()
        print("All records deleted.\n")

    elif choice == "1":
        sid = int(input("Enter ID to delete: "))
        cursor.execute("SELECT id FROM students WHERE id = ?", (sid,))
        if cursor.fetchone():
            cursor.execute("DELETE FROM students WHERE id = ?", (sid,))
            conn.commit()
            print("Student deleted.\n")
        else:
            print("Student not found.\n")

    else:
        print("Invalid choice.\n")


# View result for a student from DB
def view_result():
    sid = int(input("Enter ID to view result: "))

    cursor.execute("SELECT name, subject, marks FROM students WHERE id = ?", (sid,))
    rows = cursor.fetchall()

    if not rows:
        print("Student not found.\n")
        return

    name = rows[0][0]
    total = sum(row[2] for row in rows)
    result = "Pass" if all(row[2] >= PASS_MARK for row in rows) else "Fail"
    marks_str = ", ".join(f"{row[1]}: {row[2]}" for row in rows)

    print(f"ID: {sid} | Name: {name} | Subjects: {marks_str} | Total: {total} | Result: {result}\n")


# Helper: group DB rows by student ID into a dict
def _group_students():
    cursor.execute("SELECT id, name, subject, marks FROM students")
    rows = cursor.fetchall()
    students_dict = {}
    for sid, name, subject, mark in rows:
        if sid not in students_dict:
            students_dict[sid] = {"id": sid, "name": name, "marks": {}}
        students_dict[sid]["marks"][subject] = mark
    return students_dict


# Reports from DB
def reports():
    students_dict = _group_students()

    if not students_dict:
        print("No Records Found")
        return

    print("\n1. Total Report")
    print("2. Pass Students")
    print("3. Fail Students")

    choice = input("Enter Choice: ")

    if choice == "1":
        print("\nTotal Students:", len(students_dict))
        passed = sum(
            1 for s in students_dict.values()
            if all(m >= PASS_MARK for m in s["marks"].values())
        )
        failed = len(students_dict) - passed
        print("Pass :", passed)
        print("Fail :", failed)

    elif choice == "2":
        print("\nPass Students")
        for s in students_dict.values():
            if all(m >= PASS_MARK for m in s["marks"].values()):
                print(f"ID: {s['id']} | Name: {s['name']} | Marks: {s['marks']}")

    elif choice == "3":
        print("\nFail Students")
        for s in students_dict.values():
            if not all(m >= PASS_MARK for m in s["marks"].values()):
                print(f"ID: {s['id']} | Name: {s['name']} | Marks: {s['marks']}")

    else:
        print("Invalid Choice")


# Download PDF report from DB
def download_report():
    students_dict = _group_students()

    if not students_dict:
        print("No records found.\n")
        return

    pdf = SimpleDocTemplate(REPORT_FILE)
    elements = []
    styles = getSampleStyleSheet()

    title = Paragraph("<b><font size=18>Student Management System Report</font></b>", styles['Title'])
    elements.append(title)

    data = [["ID", "Name", "Marks", "Total", "Result"]]

    for s in students_dict.values():
        total = sum(s["marks"].values())
        result = "Pass" if all(m >= PASS_MARK for m in s["marks"].values()) else "Fail"
        marks = ", ".join([f"{subject}: {mark}" for subject, mark in s["marks"].items()])
        data.append([s["id"], s["name"], marks, total, result])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige)
    ]))

    elements.append(table)
    pdf.build(elements)
    print(f"\nPDF Report saved successfully as '{REPORT_FILE}'\n")


# Email any file as an attachment
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
    maintype, subtype = "application", "octet-stream"
    if ext == ".csv":
        maintype, subtype = "text", "csv"
    elif ext == ".db":
        maintype, subtype = "application", "x-sqlite3"
    elif ext == ".pdf":
        maintype, subtype = "application", "pdf"

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype=maintype,
            subtype=subtype,
            filename=os.path.basename(file_path)
        )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, app_password)
            smtp.send_message(msg)
        print(f"File emailed successfully to {receiver}.\n")
    except Exception as e:
        print(f"Failed to send email: {e}\n")


# Generate PDF report then email it
def email_report():
    cursor.execute("SELECT id FROM students LIMIT 1")
    if not cursor.fetchone():
        print("No records found. Add students first.\n")
        return
    download_report()        # Generate the latest PDF
    email_file(REPORT_FILE)  # Send it as attachment


def menu():
    while True:
        print(
            "\n---Student Management System---"
            "\n1. Add"
            "\n2. Update"
            "\n3. Read/View"
            "\n4. Search"
            "\n5. Delete"
            "\n6. View Result"
            "\n7. Reports"
            "\n8. Download Report (pdf)"
            "\n9. Email Report"
            "\n10. Exit"
        )
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
        elif choice == "10":   # Fixed: was "0", menu shows option 10
            print("Exiting Student Management System")
            conn.close()
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    menu()
