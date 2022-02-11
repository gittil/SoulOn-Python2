from pymongo import collection

def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso...")
    return client['soul_code_data']
    
dbname = get_database()
collection_name = dbname["itens_soulcode"]

#Exclui documento cujo ID é SC004
collection_name.delete_one({"_id" : "SC004"})
#Deleta todos os documentos
collection_name.drop()
dbname.drop_collection()

detalhes_itens = collection_name.find()
for item in detalhes_itens:
    print(item)