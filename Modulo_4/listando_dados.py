from pymongo import collection

def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso...")
    return client['soul_code_data']
    
dbname = get_database()
collection_name = dbname["itens_soulcode"]


detalhes_itens = collection_name.find()
detalhes_itens = collection_name.find({"categoria":"Online"})
detalhes_itens = collection_name.find({"$and" : [{"categoria":"Online"}, {"categoria":"Físico"}]})
detalhes_itens = collection_name.find({"nome_item":{"$regex":"^Mi"}})
for item in detalhes_itens:
    print(item)

detalhes_itens = collection_name.distinct("nome_item")
detalhes_itens = collection_name.find({"categoria":"Físico"}).limit(1)
detalhes_itens = collection_name.find({}, {"nome_item", "desconto_maximo"}).skip(2)
for item in detalhes_itens:
    print(item)