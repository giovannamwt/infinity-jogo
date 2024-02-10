import pygame 
from pygame import font
import sys
import random

#from pygame.sprite import _Group

pygame.init() 

class Heroi1():
     def __init__(self):        
         self.nome = 'Guerreiro'
         self.foto = pygame.image.load(r'images\heroi1.png')
         self.hp_inicial = 100
         self.dano = [5,6,7]

     def atacar(self):
         pass
         


         
class Heroi2():
     def __init__(self):        
         self.nome = 'Arqueiro'
         self.foto = pygame.image.load(r'images\heroi2.png')
         self.hp_inicial = 130
         self.dano = [7,8,9]

class Heroi3():
     def __init__(self):        
         self.nome = 'Mago'
         self.foto = pygame.image.load(r'images\heroi3.png')
         self.hp_inicial = 120
         self.dano = [9,10,11]

class Vilao1():
     def __init__(self):        
         self.nome = 'Morte'
         self.foto = pygame.image.load(r'images\vilao1.png')
         self.hp_inicial = 100
         self.dano = [5,6,7]

     #def morrer(self,hp,dano):
         
class Vilao2():
     def __init__(self):        
         self.nome = 'Arqueiro'
         self.foto = pygame.image.load(r'images\vilao2.png')
         self.hp_inicial = 130
         self.dano = [7,8,9]

class Vilao3():
     def __init__(self):        
         self.nome = 'Mago'
         self.foto = pygame.image.load(r'images\vilao3.png')
         self.hp_inicial = 120
         self.dano = [9,10,11]

class Jogo():
     def __init__(self):        
         #self.nome = 'Mago'
         self.bg2 = pygame.image.load(r'images\fundo2.png')
         self.bg1 = pygame.image.load(r'C:images\fundo1.png')
         self.bg3 = pygame.image.load(r'C:images\fundo3.png')
         self.hp_inicial = 120
         self.velocidade = 2
         self.dano = [9,10,11]


class Barra_de_vida(pygame.surface.Surface):
    def __init__(self, largura, altura,comprimento, hp, hp_maximo):
        self.largura = largura
        self.comprimento = comprimento
        self.altura = altura
        self.hp = hp
        self.hp_maximo = hp_maximo

    def criando_barra(self,supervida):
        calculo = self.hp/ self.hp_maximo
        pygame.draw.rect(supervida,"red",[self.largura, self.altura,self.comprimento,self.hp])
        pygame.draw.rect(supervida,"green",[self.largura, self.altura,self.comprimento * calculo ,self.hp])

         

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
txt_botao1 = fonte_texto_pequeno.render('escolher' , True , 1) 
txt_botao2 = fonte_texto_pequeno.render('atacar' , True , 1) 
heroi_escolhido = False
fase_escolhida = False


jogo = Jogo()
guerreiro = Heroi1()
vilao1 = Vilao1()
bv = Barra_de_vida(largura/9,altura/8,300,40,100)

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
    hp_heroi = guerreiro.hp_inicial
    hp_vilao = vilao1.hp_inicial
    tela.blit(guerreiro.foto, (78, 175))
    tela.blit(vilao1.foto, (400, largura/6))

   # while hp_heroi >= 1:
    # pygame.draw.rect(tela,cor_clara,[largura/9, altura/8,hp_heroi*2,10])#vida heroi
    # pygame.draw.rect(tela,cor_clara,[largura/2+100, altura/8,hp_vilao*2,10])#vida vilao

    #bv.criando_barra(60)


    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: pygame.quit()

        #coordenadas do botão   
         
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/8+10 <= mouse[0] <= largura/8+150 and altura/2+200 <= mouse[1] <= altura/2+240: 
                ataque = random.choice(guerreiro.dano)
                hp_vilao = hp_vilao - ataque
                dano = random.choice(vilao1.dano)
                hp_heroi = hp_heroi - dano



#define a cor do botão ao interagir    
    if largura/8+10 <= mouse[0] <= largura/8+150 and altura/2+200 <= mouse[1] <= altura/2+240: 
        pygame.draw.rect(tela,cor_clara,[largura/8+10, altura/2+200,140,40]) #desenho do botão
          
    else: 
        pygame.draw.rect(tela,cor_escura,[largura/8+10,altura/2+200,140,40]) #desenho do botão

    tela.blit(txt_botao2 , (largura/8+45, altura/2+207)) 


    pygame.display.update()  


while True :
    # print(heroi_escolhido)
    
    if heroi_escolhido == False: 
        escolher_heroi1()
        

    else:
        if fase_escolhida == False:
            escolher_fase1()
        else:
            batalha_fase1()

     

    