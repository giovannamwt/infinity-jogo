import pygame 
from pygame import font
import sys
import random

pygame.init() 


class BarraSaude():
    def __init__(self, x, y, altura, hp_maximo, hp_atual):
        self.x = x
        self.y = y
        self.altura = altura
        self.largura = largura
        self.hp_maximo = hp_maximo
        self.hp_atual = hp_atual

    def draw(self, tela):
        pygame.draw.rect(tela, "red", (self.x, self.y, self.hp_maximo, self.altura))
        pygame.draw.rect(tela, "green", (self.x, self.y, self.hp_atual, self.altura))

class Heroi1():
     def __init__(self):        
        self.nome = 'Guerreiro'
        self.foto = pygame.image.load('images/heroi1.png')
        self.hp_atual = 100
        self.hp_maximo = 100
        self.dano = [5,6,7]

     def atacar(self):
        pass
         
         
class Heroi2():
     def __init__(self):        
         self.nome = 'Arqueiro'
         self.foto = pygame.image.load('images/heroi2.png')
         self.hp_inicial = 130
         self.dano = [7,8,9]

class Heroi3():
     def __init__(self):        
         self.nome = 'Mago'
         self.foto = pygame.image.load('images/heroi3.png')
         self.hp_inicial = 120
         self.dano = [9,10,11]

class Vilao1():
     def __init__(self):        
         self.nome = 'Morte'
         self.foto = pygame.image.load('images/vilao1.png')
         self.hp_atual = 100
         self.hp_maximo = 100
         self.dano = [5,6,7]

     #def morrer(self,hp,dano):
         
class Vilao2():
     def __init__(self):        
         self.nome = 'Arqueiro'
         self.foto = pygame.image.load('images/vilao2.png')
         self.hp_inicial = 130
         self.dano = [7,8,9]

class Vilao3():
     def __init__(self):        
         self.nome = 'Mago'
         self.foto = pygame.image.load('images/vilao3.png')
         self.hp_inicial = 120
         self.dano = [9,10,11]

class Jogo():
     def __init__(self):        
         #self.nome = 'Mago'
         self.bg2 = pygame.image.load('images/fundo2.png')
         self.bg1 = pygame.image.load('images/fundo1.png')
         self.bg3 = pygame.image.load('images/fundo3.png')
         self.bg4 = pygame.image.load('images/fundo4.png')
         self.bg5 = pygame.image.load('images/fundo5.png')
         self.hp_inicial = 120
         self.dano = [9,10,11]


         

#Minhas variáveis
dimensoes = (800,600)
cor_da_tela = (230, 230, 230) 
tela = pygame.display.set_mode((dimensoes )) 
altura = tela.get_height() 
largura = tela.get_width() 
cor_escura = (184,177,162) 
cor_clara = (214,201,87) 
fonte=pygame.font.get_default_font()
fonte_texto_pequeno= pygame.font.SysFont(fonte,35) 
titulo1='Escolha seu herói:' 
titulo2='Escolha a fase:'
titulo3='Você Venceu!'
titulo4='Você Perdeu!'
txt_botao1 = fonte_texto_pequeno.render('escolhe' , True , 1) 
txt_botao2 = fonte_texto_pequeno.render('atacar' , True , 1) 
heroi_escolhido = False
fase_escolhida = False


jogo = Jogo()
guerreiro = Heroi1()


vilao1 = Vilao1()

pygame.display.set_caption('JOGO DA GIOVANNA') #mensagem janela

def escolher_heroi1():

    global heroi_escolhido

    tela.blit(jogo.bg1, (0, 0))
    mouse = pygame.mouse.get_pos() 

    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: 
            pygame.quit() 

#coordenadas do botão    
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/8+10 <= mouse[0] <= largura/8+150 and altura/2+200 <= mouse[1] <= altura/2+240: 
                heroi_escolhido = True

                   
#define a cor do botão ao interagir    
    if largura/8+10 <= mouse[0] <= largura/8+150 and altura/2+200 <= mouse[1] <= altura/2+240: 
        pygame.draw.rect(tela,cor_clara,[largura/8+10, altura/2+200,140,40]) #desenho do botão
          
    else: 
        pygame.draw.rect(tela,cor_escura,[largura/8+10,altura/2+200,140,40]) #desenho do botão
      
#posição do texto do texto
    tela.blit(txt_botao1 , (largura/8+30, altura/2+207)) 
    tela.blit(guerreiro.foto, (78, 175)) #coordenadas para exibição foto heroi
    fontesys=pygame.font.SysFont(fonte, 60) ##### usa a fonte padrão
    txttela = fontesys.render(titulo1, 1, (0,0,0))  ##### renderiza o texto na cor desejada
    tela.blit(txttela,(230,30)) #coordenadas do titulo
    

    pygame.display.update()  

             
def escolher_fase1():

    global fase_escolhida

    tela.blit(jogo.bg2, (0, 0))
    mouse = pygame.mouse.get_pos() 
    
    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: pygame.quit() 

#coordenadas do botão    
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/8+10 <= mouse[0] <= largura/8+150 and altura/2 <= mouse[1] <= altura/2+240: 
                fase_escolhida = True

    fontesys=pygame.font.SysFont(fonte, 60) ##### usa a fonte padrão
    txttela = fontesys.render(titulo2, 1, (0,0,0))  ##### renderiza o texto na cor desejada
    tela.blit(txttela,(230,60))



    pygame.display.update()  
    

def batalha_fase1():
    tela.blit(jogo.bg3, (0, 0))
    mouse = pygame.mouse.get_pos() 

    barra_saude_vilao = BarraSaude(largura/2+120, altura/5, 10, guerreiro.hp_maximo, guerreiro.hp_atual)
    barra_saude_vilao.draw(tela)
    barra_saude_heroi = BarraSaude(largura/4, altura/5, 10, vilao1.hp_maximo, vilao1.hp_atual)
    barra_saude_heroi.draw(tela)

    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: pygame.quit()

#coordenadas do botão    
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/8+10 <= mouse[0] <= largura/8+150 and altura/2+200 <= mouse[1] <= altura/2+240: 
                dano = random.choice(guerreiro.dano)
                guerreiro.hp_atual = guerreiro.hp_atual - dano

                danoH = random.choice(vilao1.dano)
                vilao1.hp_atual = vilao1.hp_atual - danoH
                #print(f"Tomou {dano} de dano")

#define a cor do botão ao interagir    
    if largura/8+10 <= mouse[0] <= largura/8+150 and altura/2+200 <= mouse[1] <= altura/2+240: 
        pygame.draw.rect(tela,cor_clara,[largura/8+60, altura/2+200,140,40]) #desenho do botão
          
    else: 
        pygame.draw.rect(tela,cor_escura,[largura/8+60,altura/2+200,140,40]) #desenho do botão

    tela.blit(txt_botao2 , (largura/4, altura/2+207)) 


    pygame.display.update()  

def vitoria():
    tela.blit(jogo.bg4, (0, 0))
    fontesys=pygame.font.SysFont(fonte, 60) ##### usa a fonte padrão
    txttela = fontesys.render(titulo3, 1, (0,0,0))  ##### renderiza o texto na cor desejada
    tela.blit(txttela,(230,30)) #coordenadas do titulo

    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: pygame.quit()

def derrota():
    tela.blit(jogo.bg4, (0, 0))
    fontesys=pygame.font.SysFont(fonte, 60) ##### usa a fonte padrão
    txttela = fontesys.render(titulo4, 1, (0,0,0))  ##### renderiza o texto na cor desejada
    tela.blit(txttela,(230,30)) #coordenadas do titulo

    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: pygame.quit()


while True :
    # print(heroi_escolhido)
    
    if heroi_escolhido == False: 
        escolher_heroi1()
        

    else:
        if fase_escolhida == False:
            escolher_fase1()
        else:
            batalha_fase1()

     

    