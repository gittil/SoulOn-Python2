import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin123",
  database="mydatabase"
)

mycursor = mydb.cursor()

#sql = "SELECT * FROM customers WHERE address = 'São Paulo, SP'"

sql = "SELECT * FROM customers WHERE address LIKE '%SP%'"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
  