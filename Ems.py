import mysql.connector
from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch

# open connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shubham@1978",
    database="Link_code"
)
print("Database connected successfully")

cursor = conn.cursor()

# create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS emp (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(20),
        sal DECIMAL(10,2),
        Ex INT
    )
""")


def insert_emp(conn):
    name = input("Enter your name: ")
    sal = float(input("Enter your salary: "))
    ex = int(input("Enter your experience: "))
    cursor.execute(
        "INSERT INTO emp (name, sal, Ex) VALUES (%s, %s, %s)",
        (name, sal, ex)
    )
    conn.commit()
    print("Data inserted successfully")


def delete_by_name(conn):
    emp_name = input("Enter Your name TO Delete: ")
    cursor.execute("DELETE FROM emp WHERE name=%s", (emp_name,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Employee With Name '{emp_name}' Deleted")
    else:
        print(f"No Employee Found With Name '{emp_name}'")


def delete_by_id(conn):
    emp_id = int(input("Enter Your ID TO delete: "))
    cursor.execute("DELETE FROM emp WHERE id=%s", (emp_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Employee With ID '{emp_id}' Deleted")
    else:
        print(f"No Employee Found With ID '{emp_id}'")


def show_all(conn):
    cursor.execute("SELECT * FROM emp")
    rows = cursor.fetchall()
    if not rows:
        print("No Records Found.\n")
        return
    for row in rows:
        print(f"ID: {row[0]}  Name: {row[1]}  Salary: {row[2]}  Experience: {row[3]}")
    print()


def download_emp_data_pdf(conn):
    """Generate a PDF report of all employee data, for admin use."""
    cursor.execute("SELECT id, name, sal, Ex FROM emp")
    rows = cursor.fetchall()

    if not rows:
        print("No Records Found. Nothing to export.\n")
        return

    file_name = f"emp_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Employee Data Report", styles["Title"]))
    story.append(Paragraph(
        f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        styles["Normal"]
    ))
    story.append(Spacer(1, 20))

    table_data = [["ID", "Name", "Salary", "Experience"]]
    for row in rows:
        table_data.append([str(row[0]), row[1], f"{row[2]:.2f}", str(row[3])])

    table = Table(table_data, colWidths=[0.8 * inch, 2 * inch, 1.3 * inch, 1.3 * inch])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2c3e50")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.HexColor("#f0f0f0")]),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(table)

    doc = SimpleDocTemplate(file_name, pagesize=letter)
    doc.build(story)

    print(f"Employee data exported successfully to '{file_name}'\n")


while True:
    print("1. Insert Data")
    print("2. Delete By Name")
    print("3. Delete By ID")
    print("4. Show All Data")
    print("5. Exit")
    print("6. Download Employee Data (PDF) - Admin")
    choice = input("Enter your choice: ")

    if choice == "1":
        insert_emp(conn)
    elif choice == "2":
        delete_by_name(conn)
    elif choice == "3":
        delete_by_id(conn)
    elif choice == "4":
        show_all(conn)
    elif choice == "5":
        print("Exiting the program.")
        break
    elif choice == "6":
        download_emp_data_pdf(conn)
    else:
        print("Invalid choice. Please try again.")

cursor.close()
conn.close()