import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost",
    user="root",
    password="admin123",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

