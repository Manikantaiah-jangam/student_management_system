
from decimal import Decimal, InvalidOperation

import mysql.connector

from db import get_connection


def insert_student():
    con = None

    try:
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ").strip()
        marks = Decimal(input("Enter marks: "))

        if student_id <= 0:
            print("Student ID must be positive.")
            return

        if not name:
            print("Name cannot be empty.")
            return

        if not marks.is_finite() or not Decimal("0") <= marks <= Decimal("100"):
            print("Marks must be between 0 and 100.")
            return

        con = get_connection()

        with con.cursor() as cur:
            cur.execute(
                """
                INSERT INTO students (id, name, marks)
                VALUES (%s, %s, %s)
                """,
                (student_id, name, marks)
            )

        con.commit()
        print("Student inserted successfully!")

    except (ValueError, InvalidOperation) as err:
        print("Invalid input:", err)

    except mysql.connector.Error as err:
        if con is not None and con.is_connected():
            con.rollback()
        print("Insert error:", err)

    finally:
        if con is not None and con.is_connected():
            con.close()


def display_students():
    con = None

    try:
        con = get_connection()

        with con.cursor() as cur:
            cur.execute("SELECT id, name, marks FROM students ORDER BY id")
            rows = cur.fetchall()

        if not rows:
            print("No student records found.")
            return

        for row in rows:
            print(row)

    except mysql.connector.Error as err:
        print("Display error:", err)

    finally:
        if con is not None and con.is_connected():
            con.close()


def search_student():
    try:
        student_id = int(input("Enter student ID to search: "))
    except ValueError:
        print("Enter a valid integer ID.")
        return

    con = None

    try:
        con = get_connection()

        with con.cursor() as cur:
            cur.execute(
                "SELECT id, name, marks FROM students WHERE id = %s",
                (student_id,)
            )
            row = cur.fetchone()

        if row:
            print("Student found:", row)
        else:
            print("Student not found.")

    except mysql.connector.Error as err:
        print("Search error:", err)

    finally:
        if con is not None and con.is_connected():
            con.close()


def update_student():
    con = None

    try:
        student_id = int(input("Enter student ID: "))
        marks = Decimal(input("Enter new marks: "))

        if not marks.is_finite() or not Decimal("0") <= marks <= Decimal("100"):
            print("Marks must be between 0 and 100.")
            return

        con = get_connection()

        with con.cursor() as cur:
            cur.execute(
                "UPDATE students SET marks = %s WHERE id = %s",
                (marks, student_id)
            )
            affected = cur.rowcount

        con.commit()

        if affected:
            print("Student marks updated successfully!")
        else:
            print("Student not found or marks unchanged.")

    except (ValueError, InvalidOperation) as err:
        print("Invalid input:", err)

    except mysql.connector.Error as err:
        if con is not None and con.is_connected():
            con.rollback()
        print("Update error:", err)

    finally:
        if con is not None and con.is_connected():
            con.close()


def delete_student():
    con = None

    try:
        student_id = int(input("Enter student ID to delete: "))
        confirmation = input(
            f"Delete student ID {student_id}? (yes/no): "
        ).strip().lower()

        if confirmation != "yes":
            print("Deletion cancelled.")
            return

        con = get_connection()

        with con.cursor() as cur:
            cur.execute(
                "DELETE FROM students WHERE id = %s",
                (student_id,)
            )
            affected = cur.rowcount

        con.commit()

        if affected:
            print("Student deleted successfully!")
        else:
            print("Student ID not found.")

    except ValueError:
        print("Enter a valid integer ID.")

    except mysql.connector.Error as err:
        if con is not None and con.is_connected():
            con.rollback()
        print("Delete error:", err)

    finally:
        if con is not None and con.is_connected():
            con.close()


def main():
    # Ensure the expected table exists.
    con = None

    try:
        con = get_connection()

        with con.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    marks DECIMAL(5, 2) NOT NULL
                )
            """)

        con.commit()
        print("MySQL connected successfully!")

    except (mysql.connector.Error, ValueError) as err:
        print("Database setup failed:", err)
        return

    finally:
        if con is not None and con.is_connected():
            con.close()

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
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Select 1 to 6.")


if __name__ == "__main__":
    main()
