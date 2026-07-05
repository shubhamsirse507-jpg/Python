import mysql.connector

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


while True:
    print("1. Insert Data")
    print("2. Delete By Name")
    print("3. Delete By ID")
    print("4. Show All Data")
    print("5. Exit")
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
    else:
        print("Invalid choice. Please try again.")

cursor.close()
conn.close()