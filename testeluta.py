#ataque
import random
heroi_hp = 100
vilao_hp = 100
lista = [7,8,9]

# atacar = True
# if atacar == True:
ataque = random.choice(lista)
vilao_hp = vilao_hp - ataque
print(vilao_hp)

