import mysql.connector

# 1. Connect to MySQL
try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password",
        database="college",
        port=3306
    )

    cur = con.cursor()
