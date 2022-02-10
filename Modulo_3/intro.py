import mysql.connector as mysql

db = mysql.connect(host="IP DO SEU HOST", user="SEU USUÁRIO", passwd="SUA SENHA", db="SEU DB")

cursor = db.cursor()
cursor.execute('SELECT * FROM `tblbooks`')
numrows = int(cursor.rowcount)
linhas = cursor.fetchall()

print("Número total de registros encontrados: ", numrows) 
print("\nMostrando resultados...") 
for linha in linhas: 
    print("-", linha[0]) 
    print('-', linha[1])
