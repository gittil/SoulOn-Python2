from pymongo import collection

def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso...")
    return client['soul_code_data']

def cadastrarDocumento():
    dbname = get_database()
    collection_name = dbname['itens_soulcode']

    n = int(input("Quantos campos terá seu documento? "))
    d = dict(input("Digite a chave e o valor separado por espaços: ").split() for _ in range(n))
    print(d)
    collection_name.insert_one(d)
    print("Documento inserido com sucesso!")


def mostrarDocumento():
    dbname = get_database()
    collection_name = dbname['itens_soulcode']
    detalhes_itens = collection_name.find()
    for item in detalhes_itens:
        print(item)


def deletarDocumento():
    dbname = get_database()
    collection_name = dbname['itens_soulcode']
    documento = str(input("Qual o ID do item a ser deletado?"))
    collection_name.delete_one({"_id":documento})
    print("Documento excluído com sucesso!")
    
def deletarTudo():
    var = str(input("Deseja realmente deletar tudo? S/N"))
    dbname = get_database()
    collection_name = dbname['itens_soulcode']

    if (var == 'S'):
        collection_name.drop()
        dbname.drop_collection()
    elif (var=='N'):
        print("Nenhum dado foi excluído!")


def atualizarDocumento():
    dbname = get_database()
    collection_name = dbname['itens_soulcode']
    temp = str(input("O que você deseja alterar?\n1-Atualizar por ID: \n2-Atualizar por campo: "))
    if (temp=="1"):
        id = str(input("Digite o ID as ser alterado: "))
        chave = str(input("Digite o campo a ser alterado: "))
        valor = str(input("Digite o novo valor do campo digitado: "))

        collection_name.update_one({"_id":id}, {"$set":{chave:valor}})
        print("Modificação realizada!")
    elif (temp=="2"):
        chave = str(input("Digite a chave a ser buscada: "))
        valor = str(input("Digite o valor a ser buscado: "))
        chave2 = str(input("Digite a chave a ser alterada: "))
        valor2 = str(input("Digite o novo valor: "))

        collection_name.update_many({chave:valor}, {"$set":{chave2:valor2}})
        print("Modificação realizada!")

#cadastrarDocumento()
#deletarDocumento()
#deletarTudo()
atualizarDocumento()
mostrarDocumento()




