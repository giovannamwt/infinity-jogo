class Fatura:
    
    def __init__(self, nome, preco, qtde):
        self.nome_item = nome
        self.preco = preco
        self.qtde = qtde
        #self.total = none

    def gerar_fatura(self):
        self.total = self.preco * self.qtde
        return f'O valor da sua fatura é: {self.total}'


Produto1 = Fatura(nome='mouse',preco=50, qtde=3)

print(Produto1.gerar_fatura())

Produto2 = Fatura(nome='teclado',preco=100, qtde=3)

print(Produto2.gerar_fatura())

