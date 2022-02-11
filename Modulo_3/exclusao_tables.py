import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin123",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)
print("Tabela excluída com sucesso!")
