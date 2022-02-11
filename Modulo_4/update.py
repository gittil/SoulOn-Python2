from pymongo import collection

def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso...")
    return client['soul_code_data']
    
dbname = get_database()
collection_name = dbname["itens_soulcode"]

#atualiza desconto_maximo de 10% para 35%.
collection_name.update_many({"disconto_maximo":"10%"}, 
                            {"$set":{"disconto_maximo": "35%"}})

#atualiza desconto para 100% onde nome_item tenha a palavra 'Aula'
collection_name.update_one({ "nome_item": { "$regex": "Aula" } },
                           {"$set":{"disconto_maximo": "100%"}})

detalhes_itens = collection_name.find()
for item in detalhes_itens:
    print(item)
    


