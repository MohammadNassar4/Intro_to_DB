import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '68#kcyWh9J*PjkXORu$s',
    database = 'MySQL'
    )
    print("Successfuly connected to my database")
except mysql.connector.Error as e:
    print(f"Error: {e}")

cursor = mydb.cursor()

try:
    cursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store;')
    mydb.commit()
    print("Database 'alx_book_store' created successfully!")
except Error as e:
    print(f"Error: {e}")

cursor.close()
mydb.close()