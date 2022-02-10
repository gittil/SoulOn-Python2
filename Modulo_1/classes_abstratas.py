from abc import ABC, abstractmethod

class letras():
    @abstractmethod
    def mostrarTipo(self):
        print("Eu sou uma classe abastrata!")
        
class A(letras):
    def __init__(self, descricao):
        self.descricao = descricao
        
    def imprimir(self):
        print("Aqui é um método diferente!")


letraa = A("letra A")
letraa.mostrarTipo()
letraa.imprimir()