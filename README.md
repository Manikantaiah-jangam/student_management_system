# Python + MySQL Student Management System

A menu-driven Student Management System built using Python and MySQL. This project demonstrates Python Database Connectivity (PDBC), SQL CRUD operations, database connection management, and modular Python programming.

## Overview

The Student Management System allows users to manage student records through a command-line interface. Users can add new students, view all records, search for individual students, update marks, and delete records.

The project uses MySQL to store student data persistently and Python to perform database operations.

## Features

- **Insert Student:** Add a student with an ID, name, and marks.
- **Display Students:** View all stored student records.
- **Search Student:** Find a student using their ID.
- **Update Marks:** Modify a student's marks.
- **Delete Student:** Remove a student record.
- **Database Connectivity:** Connect Python to MySQL.
- **Environment Configuration:** Store database credentials in a local `.env` file.
- **SQL Safety:** Use parameterized queries to help prevent SQL injection.

## Technologies Used

- Python
- MySQL
- MySQL Connector/Python
- python-dotenv
- SQL
- Git and GitHub

## Project Structure

```text
Simple-Project/
├── student_management_system.py
├── db.py
├── test_connection.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

**Note:** The `.env` file is required locally but must not be uploaded to GitHub. The `.gitignore` file excludes sensitive configuration and unnecessary files.

## Prerequisites

Install the following before running the project:

1. Python 3.10 or later.
2. MySQL Server.
3. Git (optional, for version control).

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/codesniper123/python-mysql-student-management.git
cd python-mysql-student-management
```

Replace the repository URL if your GitHub repository uses a different name.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Create the MySQL database

Log in to MySQL and execute:

```sql
CREATE DATABASE college;
```

The application must use a MySQL account with appropriate permissions for the database.

### 4. Configure environment variables

Create a local file named `.env` in the project directory:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=college
DB_PORT=3306
```

Replace `your_mysql_password` with your actual local database password.

**Security:** Never commit `.env` or publish database passwords. Use a dedicated database account with limited privileges when possible.

### 5. Run the connection test

```bash
python test_connection.py
```

A successful connection should display a confirmation message.

### 6. Run the application

```bash
python student_management_system.py
```

## Application Menu

```text
===== STUDENT MANAGEMENT =====
1. Insert student
2. Display all students
3. Search student
4. Update marks
5. Delete student
6. Exit

Enter your choice:
```

Choose an option from the menu and follow the prompts.

## Database Operations

| Operation | SQL command | Purpose |
|---|---|---|
| Create | `INSERT` | Add a student record |
| Read | `SELECT` | Display or search records |
| Update | `UPDATE` | Change student marks |
| Delete | `DELETE` | Remove a student record |

## Concepts Demonstrated

- Python functions and modular programming
- Database connections and cursors
- SQL queries and CRUD operations
- Parameterized queries
- Environment variables and configuration
- Exception handling
- Transaction management using `commit()` and `rollback()`
- Resource cleanup and connection closing
- Version control using Git

## Future Improvements

- Add input validation and more informative error messages.
- Add student details such as email, course, and department.
- Implement sorting, filtering, and pagination.
- Add automated tests.
- Build a REST API using Django REST Framework.
- Create a web interface for easier student record management.
- Add authentication and role-based permissions.

## Learning Outcomes

This project provides practical experience in connecting Python applications to MySQL, writing SQL queries, implementing CRUD functionality, organizing code into modules, and managing database configuration securely.

## Author

**Manikantaiah Jangam**

Computer Science and Design | B.Tech

GitHub: https://github.com/Manikantaiah-jangam

## License

This project is available for educational and learning purposes. Add an explicit open-source license if you want to grant others formal reuse and distribution rights.