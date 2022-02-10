class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class CarrinhoCompras:
    def __init__(self, ):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(f'{produto.nome}: R${produto.valor}')

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return f'R${total}'
    
    
carrinho = CarrinhoCompras()
p1 = Produto('Boné', 50)
p2 = Produto('Tênis', 100)
p3 = Produto('Camiseta', 39)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.lista_produtos()
print(carrinho.soma_total())