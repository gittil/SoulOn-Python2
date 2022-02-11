import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin123",
  database="mydatabase"
)

mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Manaus, AM' WHERE address = 'Palmas, TO'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "linha(s) afetada(s).")