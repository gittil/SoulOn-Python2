import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin123",
  database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT name, address FROM customers")

'''
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''
myresult = mycursor.fetchone()
print(myresult)
