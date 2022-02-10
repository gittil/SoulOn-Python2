#criando a classe Veiculo
from calendar import c


class Veiculo():
    #metodo __init__ é o construtor, todos os atributos que forem declarados nesse metodo são obrigatórios para criar o objeto
    def __init__(self, tipo, chassi, marca, modelo, ano):
        #quando utilizamos o self estamos dizendo que são caracteristicas relacionada a ele mesmo
        #os atributos são as caracteristicas que nosso objeto tem
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

#criando a classe Aviao
class Aviao():
    def __init__(self, tipo, motor, linha_aerea, modelo, ano):
        self.tipo = tipo
        self.motor = motor
        self.linha_aerea = linha_aerea
        self.modelo = modelo
        self.ano = ano

#instanciando objeto Veiculo
objeto_carro = Veiculo('carro','456dfd564gf5d64g65dfg','Marca X', 'X1','2022')
print(vars(objeto_carro))

objeto_aviao = Aviao('monomotor','500HP','XXX','X10','2000')
print(vars(objeto_aviao))

class Funcionario():
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    
    #criando metodos
    def get_salario(self):
        print("Meu salário é: ", self.salario)
        
    def get_bonificacao(self):
        return self.salario * 0.15
    
funcionario1 = Funcionario("João","798465132", 5000)

funcionario1.get_salario()

print(funcionario1.get_bonificacao())
        
#encapsulamento
class Func():
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0 # dois __ siginifica que o atributo é privado
        self.__horas_trabalhadas = 0 #private
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("Impossível alterar salário diretamente, usa a função calcula_salario().")
    
    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1
        
    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada
        
funcionario2 = Func('José','Professor', 50)

# se utilizar o método salário não irá funcionar pois o método só existe dentro da classe
#funcionario2.salario = 10000

class Veiculo2():
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca 
        self.modelo = modelo 
        self.ano = ano 
        
class Motocicleta(Veiculo2):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.cilindrada = cilindrada
print("------------------------------------------------")
v = Veiculo2('carro','456456fdfdf','X','X15','1999')
print(vars(v))
print("------------------------------------------------")
m = Motocicleta('motoca','4564df4ds65f4ds','F','motoneta','1950', 1000)
print(vars(m))
                