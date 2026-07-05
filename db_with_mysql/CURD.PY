from db import conn, cursor
#insert
def insert_emp(conn, data):
    name=input("Enter your name: ")
    sal=float(input("Enter your salary: "))
    ex=int(input("Enter your experience: "))
    cursor.execute("INSERT INTO emp (name, sal, Ex) VALUES (%s, %s, %s)", (name, sal, ex))
    conn.commit()
    print("data inserted successfully")