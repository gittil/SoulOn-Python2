import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin123",
  database="mydatabase"
)

mycursor = mydb.cursor()

#sql = "SELECT name FROM customers ORDER BY name"
sql = "SELECT name FROM  customers ORDER BY name DESC"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
      print(x)