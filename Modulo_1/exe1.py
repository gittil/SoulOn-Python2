# exercicio 1
# Crie uma classe animal com atributos e métodos, posteriormente, crie uma classe que herde seus atributos, e possuía os seus atributos próprios. 
# Crie dois objetos da classe filha.

class Animal():
    def __init__(self, raça):
        self.raça = raça 
        
class Cachorro(Animal):
    def __init__(self, raça, porte, pelagem):
        super().__init__(raça)
        self.porte = porte 
        self.pelagem = pelagem 
        
cachorro1 = Cachorro("Dog Alemão","Grande","curta")
print(vars(cachorro1))
print("------------------------------------------------------------")
cachorro2 = Cachorro("Poodle","Pequeno","longa")
print(vars(cachorro2))
