
object

class Gato:
	#nome = 'Batman'
	#idade = 12 # idade em meses
	cor = 'preto'
	raça = 'Persa'
	
def __init__(self, nome, idade):  #só existem esses atributos após instanciar a classe
        self.nome = 'Batman'
        self.idade = 8


def ronronar(self):
		print("ronron")

def falar(self):
		print("miau")

def pular(self):
	print("pulando...")
		

batman = Gato(nome='caju',idade=5) # instanciando a classe


print(Gato.idade)
print(Gato.raça)
print(batman.ronronar())