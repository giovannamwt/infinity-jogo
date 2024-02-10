import pygame
pygame.init()

tela = pygame.display.set_mode([800,500])

rodando = True
while rodando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill((255, 255, 255))

    # pygame.draw.circle(tela, (0, 0, 255), (250, 250), 75)
    #tela = pygame.display.set_mode(size)
    pygame.display.set_caption('Pokemon Battle')

    pygame.display.flip()

pygame.quit()









































# class Personagem:
#     def __init__(self, nome, nivel, classe, pontuacao):
#         self.nome_item = nome
#         self.nivel = nivel
#         self.classe = classe
#         self.pontuacao = pontuacao

#     def atacar(self):
#         pass

#     def defender(self):
#         pass

#     def receber_dano():
#         pass

# class Heroi(Personagem):
#     pass

# class Inimigo(Personagem):
#     pass
