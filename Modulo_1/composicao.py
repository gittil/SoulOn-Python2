# Composição

class Cliente:
    def __init__(self, nome):
        self.__nome = nome 
        self.__enderecos = []
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter 
    def nome(self,nome):
        self.__nome = nome
        
    def inserir_endereco(self, cidade):
        self.__enderecos.append(Endereco(cidade))
        
    def lista_enderecos(self):
        for endereco in self.__enderecos:
            print(endereco.cidade)
            
class Endereco():
    def __init__(self,cidade):
        self.__cidade = cidade
        
    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade
        

cliente1 = Cliente("José")
cliente1.inserir_endereco("São Paulo")
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1

