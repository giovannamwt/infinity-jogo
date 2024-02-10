
class Banco:
    def __init__(self, id, nome, saldo):
        self.id = id
        self.nome = nome
        self.saldo = saldo
    def infos(self):
        return f'\n id :{self.id} \n nome : {self.nome} \n saldo: R${self.saldo},00'


class Corrente(Banco):
    #pass
    print("hello")


class Poupanca(Banco):
    def novoSaldo(self):
        self.nSaldo = float(input("Insira um valor para adcionar:"))
        self.saldo = self.saldo + self.nSaldo
        return f'Novo saldo {self.saldo}'
    # def infos(self):
    #     pass
    # def infos(self):
    #     pass
    

ana = Poupanca(999, 'Ana', 2350)
#jo = Poupanca(888, 'Jó', 500)
#mingau = Gato('Mingau')

print(ana.infos())
print(ana.novoSaldo())
#print(ana.infos())
#print(mingau.nome, 'faz', mingau.fazerSom())


