# import pygame 
# from pygame import font
# import sys






    # # evento de tecla pressionada
    # if event.type == pygame.KEYDOWN:
               
    #         # checking if key "A" was pressed
    #         if event.key == pygame.K_a:
    #             print("Key A has been pressed")
               
    #         # checking if key "J" was pressed
    #         if event.key == pygame.K_j:
    #             print("Key J has been pressed")





#Mostra o objeto de tela/superfície de exibição na janela do pygame    

#tela.fill(cor_da_tela)  
#tela.fill((60,25,60)) 
 #pygame.font.init()

import pygame
import os
from pygame.locals import *
from sys import exit


menu_selecao = 1
WIDTH = 1000
HEIGHT = 800
FPS = 30

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
botao_enter = False


def eventos():

    global menu_selecao, botao_enter
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_s:
                menu_selecao += 1
            if event.key == K_w:
                menu_selecao -= 1
            if event.key == K_ESCAPE:
                menu_selecao += 10

    def selecao():

        global menu_selecao, botao_enter

        if menu_selecao == 1:

            screen.fill((0, 0, 0))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            novo_jogo = fonte.render('>> Novo jogo <<', True, (80, 80, 80))
            screen.blit(novo_jogo, ((WIDTH/2)-55, (HEIGHT/2)))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            carregar_jogo = fonte.render(' Carregar jogo ', True, (80, 80, 80))
            screen.blit(carregar_jogo, ((WIDTH / 2) - 50, (HEIGHT / 2)+22))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            configuracoes = fonte.render(' Configurações ', True, (80, 80, 80))
            screen.blit(configuracoes, ((WIDTH / 2) - 50, (HEIGHT / 2)+44))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            sobre = fonte.render(' Sobre ', True, (80, 80, 80))
            screen.blit(sobre, ((WIDTH / 2) - 20, (HEIGHT / 2)+66))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            sair = fonte.render(' Sair ', True, (80, 80, 80))
            screen.blit(sair, ((WIDTH / 2) - 15, (HEIGHT / 2)+88))

        if menu_selecao == 2:

            screen.fill([0, 0, 0])

            fonte = pygame.font.SysFont('arial', 20, False, False)
            novo_jogo = fonte.render(' Novo jogo ', True, (80, 80, 80))
            screen.blit(novo_jogo, ((WIDTH / 2) - 55, (HEIGHT / 2)))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            carregar_jogo = fonte.render('>> Carregar jogo <<', True, (80, 80, 80))
            screen.blit(carregar_jogo, ((WIDTH / 2) - 50, (HEIGHT / 2) + 22))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            configuracoes = fonte.render(' Configurações ', True, (80, 80, 80))
            screen.blit(configuracoes, ((WIDTH / 2) - 50, (HEIGHT / 2) + 44))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            sobre = fonte.render(' Sobre ', True, (80, 80, 80))
            screen.blit(sobre, ((WIDTH / 2) - 20, (HEIGHT / 2) + 66))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            sair = fonte.render(' Sair ', True, (80, 80, 80))
            screen.blit(sair, ((WIDTH / 2) - 15, (HEIGHT / 2) + 88))

            if menu_selecao == 3:

                screen.fill(0, 0, 0)

            fonte = pygame.font.SysFont('arial', 20, False, False)
            novo_jogo = fonte.render(' Novo jogo ', True, (80, 80, 80))
            screen.blit(novo_jogo, ((WIDTH/2)-55, (HEIGHT/2)))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            carregar_jogo = fonte.render(' Carregar jogo ', True, (80, 80, 80))
            screen.blit(carregar_jogo, ((WIDTH / 2) - 50, (HEIGHT / 2)+22))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            configuracoes = fonte.render('>> Configurações <<', True, (80, 80, 80))
            screen.blit(configuracoes, ((WIDTH / 2) - 50, (HEIGHT / 2)+44))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            sobre = fonte.render(' Sobre ', True, (80, 80, 80))
            screen.blit(sobre, ((WIDTH / 2) - 20, (HEIGHT / 2)+66))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            sair = fonte.render(' Sair ', True, (80, 80, 80))
            screen.blit(sair, ((WIDTH / 2) - 15, (HEIGHT / 2)+88))

            if menu_selecao == 4:

                screen.fill(0, 0, 0)

            fonte = pygame.font.SysFont('arial', 20, False, False)
            novo_jogo = fonte.render(' Novo jogo ', True, (80, 80, 80))
            screen.blit(novo_jogo, ((WIDTH/2)-55, (HEIGHT/2)))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            carregar_jogo = fonte.render(' Carregar jogo ', True, (80, 80, 80))
            screen.blit(carregar_jogo, ((WIDTH / 2) - 50, (HEIGHT / 2)+22))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            configuracoes = fonte.render(' Configurações ', True, (80, 80, 80))
            screen.blit(configuracoes, ((WIDTH / 2) - 50, (HEIGHT / 2)+44))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            sobre = fonte.render('>> Sobre <<', True, (80, 80, 80))
            screen.blit(sobre, ((WIDTH / 2) - 20, (HEIGHT / 2)+66))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            sair = fonte.render(' Sair ', True, (80, 80, 80))
            screen.blit(sair, ((WIDTH / 2) - 15, (HEIGHT / 2)+88))

        if menu_selecao == 5:

            screen.fill(0, 0, 0)

            fonte = pygame.font.SysFont('arial', 20, False, False)
            novo_jogo = fonte.render(' Novo jogo ', True, (80, 80, 80))
            screen.blit(novo_jogo, ((WIDTH / 2) - 55, (HEIGHT / 2)))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            carregar_jogo = fonte.render(' Carregar jogo ', True, (80, 80, 80))
            screen.blit(carregar_jogo, ((WIDTH / 2) - 50, (HEIGHT / 2) + 22))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            configuracoes = fonte.render(' Configurações ', True, (80, 80, 80))
            screen.blit(configuracoes, ((WIDTH / 2) - 50, (HEIGHT / 2) + 44))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            sobre = fonte.render(' Sobre ', True, (80, 80, 80))
            screen.blit(sobre, ((WIDTH / 2) - 20, (HEIGHT / 2) + 66))

            fonte = pygame.font.SysFont('arial', 20, False, False)
            sair = fonte.render('>> Sair <<', True, (80, 80, 80))
            screen.blit(sair, ((WIDTH / 2) - 15, (HEIGHT / 2) + 88))

        if menu_selecao == 6:
            menu_selecao = 5

        if menu_selecao == 0:
            menu_selecao = 1

        if menu_selecao == 14:
            menu_selecao = 400

        if menu_selecao == 400:

            screen.fill(0, 0, 0)

            fonte = pygame.font.SysFont('arial', 20, False, False)
            fonte_render = fonte.render('----Criado por Marvin Marjan----', True, (100, 245, 250))
            fonte_render2 = fonte.render('----                Versão 0.1                  ----', True, (247, 142, 67))
            voltar_render = fonte.render('>> Voltar <<', True, (80, 80, 80))
            screen.blit(fonte_render, ((WIDTH / 2) - 130, (HEIGHT / 2)))
            screen.blit(fonte_render, ((WIDTH / 2) - 130, (HEIGHT / 2) + 20))
            screen.blit(fonte_render, ((WIDTH / 2) - 45, (HEIGHT / 2) + 300))

            if menu_selecao == 401:
                menu_selecao = 400
            if menu_selecao == 399:
                menu_selecao = 400

            if menu_selecao == 410:
                menu_selecao = 4

            if menu_selecao == 15:
                menu_selecao = 500

            if menu_selecao == 500:
                pygame.quit()
                exit()

        while True:
            print(botao_enter)
            print(menu_selecao)

            clock.tick(FPS)
            eventos()
            selecao()

            pygame.display.set_mode([1000, 800])

            pygame.display.update()