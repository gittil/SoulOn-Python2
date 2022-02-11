import mysql.connector

def create_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin123",
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE sistema_escolar_soul_on")
    print("Database criada com sucesso!")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",
    database="sistema_escolar_soul_on"
)
mycursor = mydb.cursor()

def create_table():
    mycursor.execute("CREATE TABLE alunos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), matricula VARCHAR(255), turma VARCHAR(255))")
    print("Tabela criada com sucesso!")

    
def insert_data():
    sql = "INSERT INTO alunos (nome, matricula, turma) VALUES (%s,%s,%s)"
    val = [
        ('José Lima','MAT90551','BCW22'),
        ('Carlos Augusto','MAT90552','BCW22'),
        ('Lívia Lima','MAT90553','BCW22'),
        ('Sandra Gomes','MAT90554','BCW23'),
        ('João Augusto','MAT90555','BCW23'),
        ('Breno Lima','MAT90556','BCW24'),
        ('José Vinícius','MAT90557','BCW25')
    ]
    
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "linha(s) inserida(s).")
    
def select_data():
    #mycursor.execute("SELECT * FROM alunos")
    #mycursor.execute("SELECT nome, matricula FROM alunos WHERE turma = 'BCW23'")
    mycursor.execute("SELECT nome FROM alunos WHERE nome LIKE '%Lima%'")

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        
def change_class():
    sql = "UPDATE alunos SET turma = 'BCW25' WHERE id = '2'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "linha(s) alterada(s). ")
    
def delete_item():
    sql = "DELETE FROM alunos WHERE id = '7'"
    mycursor.execute(sql)
    mydb.commit()

    print(mycursor.rowcount, "linha(s) deletada(s). ")