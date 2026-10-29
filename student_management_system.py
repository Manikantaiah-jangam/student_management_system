
import mysql.connector

# 1. Connect to MySQL
try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mani@3810#45",
        database="college",
        port=3306
    )

    cur = con.cursor()

    # 2. Create the table if it does not exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            marks DECIMAL(5, 2) NOT NULL
        )
    """)

    con.commit()
    print("Connected to MySQL successfully!")

except mysql.connector.Error as err:
    print("Database connection error:", err)
    raise SystemExit(1)


# 3. Insert a student
def insert_student():
    try:
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ").strip()
        marks = float(input("Enter marks: "))

        if not name:
            print("Name cannot be empty.")
            return

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        cur.execute(
            "INSERT INTO students (id, name, marks) VALUES (%s, %s, %s)",
            (student_id, name, marks)
        )

        con.commit()
        print("Student inserted successfully!")

    except (ValueError, mysql.connector.Error) as err:
        con.rollback()
        print("Insert error:", err)


# 4. Display all students
def display_students():
    cur.execute("SELECT * FROM students ORDER BY id")
    rows = cur.fetchall()

    if not rows:
        print("No student records found.")
        return

    for row in rows:
        print(row)


# 5. Search for a student
def search_student():
    student_id = input("Enter student ID to search: ")

    try:
        student_id = int(student_id)
    except ValueError:
        print("Enter a valid integer ID.")
        return

    cur.execute(
        "SELECT * FROM students WHERE id = %s",
        (student_id,)
    )

    row = cur.fetchone()

    if row:
        print("Student found:", row)
    else:
        print("Student not found.")


# 6. Update student marks
def update_student():
    try:
        student_id = int(input("Enter student ID: "))
        marks = float(input("Enter new marks: "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        cur.execute(
            "UPDATE students SET marks = %s WHERE id = %s",
            (marks, student_id)
        )

        con.commit()

        if cur.rowcount:
            print("Student marks updated!")
        else:
            print("Student ID not found.")

    except (ValueError, mysql.connector.Error) as err:
        con.rollback()
        print("Update error:", err)


# 7. Delete a student
def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))

        cur.execute(
            "DELETE FROM students WHERE id = %s",
            (student_id,)
        )

        con.commit()

        if cur.rowcount:
            print("Student deleted successfully!")
        else:
            print("Student ID not found.")

    except (ValueError, mysql.connector.Error) as err:
        con.rollback()
        print("Delete error:", err)


# 8. Menu-driven application
try:
    while True:
        print("""
===== STUDENT MANAGEMENT =====
1. Insert student
2. Display all students
3. Search student
4. Update marks
5. Delete student
6. Exit
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            insert_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Select 1 to 6.")

except mysql.connector.Error as err:
    print("Database error:", err)

finally:
    cur.close()
    con.close()
    print("Database connection closed.")
