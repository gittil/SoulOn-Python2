import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin123",
  database="mydatabase"
)

mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("José", "Piracuruca, PI")
#mycursor.execute(sql, val)
val = [
    ('Pedro', 'São Paulo, SP'), 
    ('Ana', 'Vitória, ES'),
    ('Débora', 'Palmas, TO'),
    ('Clara', 'São Bernardo, SP'),
    ('Sandy', 'Ubajara, CE')
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "linha(s) alterada(s)!")
