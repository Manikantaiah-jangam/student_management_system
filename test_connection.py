from db import get_connection

con = None

try:
    con = get_connection()
    print("MySQL connected successfully!")

except Exception as err:
    print("Connection failed:", err)

finally:
    if con is not None:
        con.close()
        print("Connection closed.")