class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazerSom(self):
        pass
class Cachorro(Animal):
    def fazerSom(self):
        return 'auau'
class Gato(Animal):
    def fazerSom(self):
        return 'miau'
    
rex = Cachorro('Rex')
mingau = Gato('Mingau')

print(rex.nome, 'faz', rex.fazerSom())
print(mingau.nome, 'faz', mingau.fazerSom())