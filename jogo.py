import pygame 
from pygame import font
import sys
import random
import sqlite3

pygame.init() 

class Personagem():
    def __init__(self, nome, foto, hp_atual, hp_maximo, dano, animacao_ataque):
        self.nome = nome
        self.foto = pygame.image.load(f"images/{foto}")
        self.hp_atual = hp_atual
        self.hp_maximo = hp_maximo
        self.dano = dano
        self.animacao_ataque = animacao_ataque

nome_do_arquivo = 'jogo.db'
conn = sqlite3.connect(nome_do_arquivo)
cursor = conn.cursor()

# Consulta para pegar os dados dos heróis
cursor.execute('''SELECT nome, foto, hp_atual, hp_maximo, dano, animacao_ataque FROM personagem''')

resultados = cursor.fetchall()

# Criar personagens
herois = []
viloes = []

for resultado in resultados:
    nome, foto, hp_atual, hp_maximo, dano, animacao_ataque = resultado
    personagem = Personagem(nome, foto, hp_atual, hp_maximo, eval(dano), animacao_ataque)
    if "heroi" in foto:
        herois.append(personagem)
    elif "vilao" in foto:
        viloes.append(personagem)


conn.close()


primeiro_heroi = herois[0]
print("Nome do primeiro herói:", primeiro_heroi.nome)


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

class AnimacaoAtaque():
    def __init__(self, arquivo, inverter, x, y):
        self.x = x
        self.y = y
        self.arquivo = arquivo
        self.inverter = inverter

    def draw(self, tela):
        for i in range(1,7):
            path = f"animations/{self.arquivo}/{i}.png"
            #print(f"Desenhando imagem {path}")
            imagem = pygame.image.load(path)

            if self.inverter:
                imagem = pygame.transform.flip(imagem, True, False)

            
            rect = imagem.get_rect()
            rect.center = (self.x, self.y)
            tela.blit((imagem), rect)
            pygame.display.update()
            pygame.time.wait(50)
            
class Heroi3():
     def __init__(self):        
         self.nome = 'Mago'
         self.foto = pygame.image.load('images/heroi3.png')
         self.hp_atual = 120
         self.hp_maximo = 120
         self.dano = [9,10,11]

class Vilao3():
     def __init__(self):        
         self.nome = 'Mago'
         self.foto = pygame.image.load('images/vilao3.png')
         self.hp_atual = 120
         self.hp_maximo = 120
         self.dano = [9,10,11]

class Jogo():
     def __init__(self, ):        
         #self.nome = 'Mago'
         self.bg2 = pygame.image.load('images/fundo2.png')
         self.bg1 = pygame.image.load('images/fundo1.png')
         self.bg3 = pygame.image.load('images/fundo3.png')
         self.bg4 = pygame.image.load('images/fundo4.png')
         self.bg5 = pygame.image.load('images/fundo5.png')
         self.bg6 = pygame.image.load('images/fundo6.png')
         self.bg7 = pygame.image.load('images/fundo7.png')
         self.bg8 = pygame.image.load('images/fundo8.png')
         self.bg9 = pygame.image.load('images/fundo9.png')
         self.bg10 = pygame.image.load('images/fundo10.png')
         self.bg11 = pygame.image.load('images/fundo11.png')

  
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
txt_botao1 = fonte_texto_pequeno.render('escolher' , True , 1) 
txt_botao2 = fonte_texto_pequeno.render('atacar' , True , 1) 
txt_botao3 = fonte_texto_pequeno.render('continuar' , True , 1) 
heroi_escolhido = False
fase_escolhida = False
ganhador = 0
continuar = False
num_heroi = 0
num_fase = 0


jogo = Jogo()
guerreiro = herois[0]
vilao1 = viloes[0]
vilao2 = viloes[1]
arqueiro = herois[1]


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
    fontesys=pygame.font.SysFont(fonte, 60) ##### usa a fonte padrão
    txttela = fontesys.render(titulo1, 1, (0,0,0))  ##### renderiza o texto na cor desejada
    tela.blit(txttela,(230,30)) #coordenadas do titulo
    

    pygame.display.update()  

def escolher_heroi2():

    #global heroi_escolhido
    global num_heroi

    tela.blit(jogo.bg6, (0, 0))
    mouse = pygame.mouse.get_pos() 

    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: 
            pygame.quit() 

#coordenadas do botão    
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/8+10 <= mouse[0] <= largura/8+150 and altura/2+200 <= mouse[1] <= altura/2+240: 
               # heroi_escolhido = True
                num_heroi = 1
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/3+80 <= mouse[0] <= largura/3+220 and altura/2+200 <= mouse[1] <= altura/2+240: 
               # heroi_escolhido = True
                num_heroi = 2
                print('heroi 2')

                   
#botão 1   
    if largura/8+10 <= mouse[0] <= largura/8+150 and altura/2+200 <= mouse[1] <= altura/2+240: 
        pygame.draw.rect(tela,cor_clara,[largura/8+10, altura/2+200,140,40]) #desenho do botão        
    else: 
        pygame.draw.rect(tela,cor_escura,[largura/8+10,altura/2+200,140,40]) #desenho do botão

#botão 2
    if largura/3+80 <= mouse[0] <= largura/3+220 and altura/2+200 <= mouse[1] <= altura/2+240: 
        pygame.draw.rect(tela,cor_clara,[largura/3+80, altura/2+200,140,40]) #desenho do botão        
    else: 
        pygame.draw.rect(tela,cor_escura,[largura/3+80,altura/2+200,140,40]) #desenho do botão
      
#posição do texto do texto
    tela.blit(txt_botao1 , (largura/8+30, altura/2+207))
    tela.blit(txt_botao1 , (largura/3+102, altura/2+207))
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
            if largura/8 <= mouse[0] <= largura/8+140 and altura/3 <= mouse[1] <= altura/3+200: 
                fase_escolhida = True

    fontesys=pygame.font.SysFont(fonte, 60) ##### usa a fonte padrão
    txttela = fontesys.render(titulo2, 1, (0,0,0))  ##### renderiza o texto na cor desejada
    tela.blit(txttela,(230,60))

    pygame.display.update()  

def escolher_fase2():

    global fase_escolhida
    global num_fase

    tela.blit(jogo.bg7, (0, 0))
    mouse = pygame.mouse.get_pos() 
    
    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: pygame.quit() 

#coordenadas do botão 1   
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/8 <= mouse[0] <= largura/8+140 and altura/3 <= mouse[1] <= altura/3+200: 
                fase_escolhida = True
                num_fase = 1
#coordenadas do botão 1=2  
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/3+60 <= mouse[0] <= largura/3+200 and altura/3 <= mouse[1] <= altura/3+140: 
                fase_escolhida = True
                num_fase = 2        

    ###pygame.draw.rect(tela,cor_escura,[largura/3+60,altura/3,140,200])
    fontesys=pygame.font.SysFont(fonte, 60) ##### usa a fonte padrão
    txttela = fontesys.render(titulo2, 1, (0,0,0))  ##### renderiza o texto na cor desejada
    tela.blit(txttela,(230,60))



    pygame.display.update()  
    
def batalha_fase1():

    global ganhador

    ataque_jogador = AnimacaoAtaque(guerreiro.animacao_ataque, False, 380, 250)
    ataque_inimigo = AnimacaoAtaque(vilao1.animacao_ataque, True, 200, 200)
    


    tela.blit(jogo.bg3, (0, 0))
    mouse = pygame.mouse.get_pos() 
   

    barra_saude_vilao = BarraSaude(largura/2+100, altura/5, 10, vilao1.hp_maximo, vilao1.hp_atual)
    barra_saude_vilao.draw(tela)
    barra_saude_heroi = BarraSaude(largura/4, altura/5, 10, guerreiro.hp_maximo, guerreiro.hp_atual)
    barra_saude_heroi.draw(tela)

    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: pygame.quit()

#coordenadas do botão    
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/8+70 <= mouse[0] <= largura/8+210 and altura/2+200 <= mouse[1] <= altura/2+240: 
                if guerreiro.hp_atual > 0 and vilao1.hp_atual > 0:
                    dano = random.choice(guerreiro.dano)
                    vilao1.hp_atual = vilao1.hp_atual - dano

                    danoH = random.choice(vilao1.dano)
                    guerreiro.hp_atual = guerreiro.hp_atual - danoH
                    

                    ataque_jogador.draw(tela)
                    ataque_inimigo.draw(tela)

                else:
                    if guerreiro.hp_atual <= 0:
                        ganhador = 2
                    else:
                        ganhador = 1
                       
#define a cor do botão ao interagir    
    if largura/8+70 <= mouse[0] <= largura/8+210 and altura/2+200 <= mouse[1] <= altura/2+240: 
        pygame.draw.rect(tela,cor_clara,[largura/8+70, altura/2+200,140,40]) #desenho do botão
          
    else: 
        pygame.draw.rect(tela,cor_escura,[largura/8+70,altura/2+200,140,40]) #desenho do botão

    tela.blit(txt_botao2 , (largura/8+105, altura/2+207)) 


    pygame.display.update()  

def batalha_fase1_h2():

    global ganhador
    ataque_jogador = AnimacaoAtaque(arqueiro.animacao_ataque, False, 380, 250)
    ataque_inimigo = AnimacaoAtaque(vilao1.animacao_ataque, True, 200, 200)



    tela.blit(jogo.bg10, (0, 0))
    mouse = pygame.mouse.get_pos() 
   

    barra_saude_vilao = BarraSaude(largura/2+100, altura/5, 10, vilao1.hp_maximo, vilao1.hp_atual)
    barra_saude_vilao.draw(tela)
    barra_saude_heroi = BarraSaude(largura/4, altura/5, 10, arqueiro.hp_maximo, arqueiro.hp_atual)
    barra_saude_heroi.draw(tela)

    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: pygame.quit()

#coordenadas do botão    
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/8+70 <= mouse[0] <= largura/8+210 and altura/2+200 <= mouse[1] <= altura/2+240: 
                if arqueiro.hp_atual > 0 and vilao1.hp_atual > 0:
                    dano = random.choice(guerreiro.dano)
                    vilao1.hp_atual = vilao1.hp_atual - dano

                    danoH = random.choice(vilao1.dano)
                    arqueiro.hp_atual = arqueiro.hp_atual - danoH
                    

                    ataque_jogador.draw(tela)
                    ataque_inimigo.draw(tela)

                    print(ganhador)
                else:
                    if arqueiro.hp_atual <= 0:
                        ganhador = 2
                        print(ganhador)
                    else:
                        ganhador = 1
                        print(ganhador)

                #print(f"Tomou {dano} de dano")

#define a cor do botão ao interagir    
    if largura/8+70 <= mouse[0] <= largura/8+210 and altura/2+200 <= mouse[1] <= altura/2+240: 
        pygame.draw.rect(tela,cor_clara,[largura/8+70, altura/2+200,140,40]) #desenho do botão
          
    else: 
        pygame.draw.rect(tela,cor_escura,[largura/8+70,altura/2+200,140,40]) #desenho do botão

    tela.blit(txt_botao2 , (largura/8+105, altura/2+207)) 


    pygame.display.update()  

def batalha_fase2_h1():

    global ganhador
    ataque_jogador = AnimacaoAtaque(arqueiro.animacao_ataque, False, 380, 250)
    ataque_inimigo = AnimacaoAtaque(vilao2.animacao_ataque, True, 200, 200)


    tela.blit(jogo.bg8, (0, 0))
    mouse = pygame.mouse.get_pos() 
   

    barra_saude_vilao = BarraSaude(largura/2+100, altura/5, 10, vilao2.hp_maximo, vilao2.hp_atual)
    barra_saude_vilao.draw(tela)
    barra_saude_heroi = BarraSaude(largura/4, altura/5, 10, guerreiro.hp_maximo, guerreiro.hp_atual)
    barra_saude_heroi.draw(tela)

    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: pygame.quit()

#coordenadas do botão    
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/8+70 <= mouse[0] <= largura/8+210 and altura/2+200 <= mouse[1] <= altura/2+240: 
                if guerreiro.hp_atual > 0 and vilao2.hp_atual > 0:
                    dano = random.choice(guerreiro.dano)
                    vilao2.hp_atual = vilao2.hp_atual - dano

                    danoH = random.choice(vilao2.dano)
                    guerreiro.hp_atual = guerreiro.hp_atual - danoH
                    

                    ataque_jogador.draw(tela)
                    ataque_inimigo.draw(tela)

                    print(ganhador)
                else:
                    if arqueiro.hp_atual <= 0:
                        ganhador = 2
                        print(ganhador)
                    else:
                        ganhador = 1
                        print(ganhador)

                #print(f"Tomou {dano} de dano")

#define a cor do botão ao interagir    
    if largura/8+70 <= mouse[0] <= largura/8+210 and altura/2+200 <= mouse[1] <= altura/2+240: 
        pygame.draw.rect(tela,cor_clara,[largura/8+70, altura/2+200,140,40]) #desenho do botão
          
    else: 
        pygame.draw.rect(tela,cor_escura,[largura/8+70,altura/2+200,140,40]) #desenho do botão

    tela.blit(txt_botao2 , (largura/8+105, altura/2+207)) 


    pygame.display.update()  

def batalha_fase2_h2():

    global ganhador
    ataque_jogador = AnimacaoAtaque(arqueiro.animacao_ataque, False, 380, 250)
    ataque_inimigo = AnimacaoAtaque(vilao2.animacao_ataque, True, 200, 200)


    tela.blit(jogo.bg9, (0, 0))
    mouse = pygame.mouse.get_pos() 
   

    barra_saude_vilao = BarraSaude(largura/2+100, altura/5, 10, vilao2.hp_maximo, vilao2.hp_atual)
    barra_saude_vilao.draw(tela)
    barra_saude_heroi = BarraSaude(largura/4, altura/5, 10, arqueiro.hp_maximo, arqueiro.hp_atual)
    barra_saude_heroi.draw(tela)

    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: pygame.quit()

#coordenadas do botão    
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/8+70 <= mouse[0] <= largura/8+210 and altura/2+200 <= mouse[1] <= altura/2+240: 
                if arqueiro.hp_atual > 0 and vilao2.hp_atual > 0:
                    dano = random.choice(arqueiro.dano)
                    vilao2.hp_atual = vilao2.hp_atual - dano

                    danoH = random.choice(vilao2.dano)
                    arqueiro.hp_atual = arqueiro.hp_atual - danoH
                    

                    ataque_jogador.draw(tela)
                    ataque_inimigo.draw(tela)

                    print(ganhador)
                else:
                    if arqueiro.hp_atual <= 0:
                        ganhador = 2
                        print(ganhador)
                    else:
                        ganhador = 1
                        print(ganhador)

                #print(f"Tomou {dano} de dano")

#define a cor do botão ao interagir    
    if largura/8+70 <= mouse[0] <= largura/8+210 and altura/2+200 <= mouse[1] <= altura/2+240: 
        pygame.draw.rect(tela,cor_clara,[largura/8+70, altura/2+200,140,40]) #desenho do botão
          
    else: 
        pygame.draw.rect(tela,cor_escura,[largura/8+70,altura/2+200,140,40]) #desenho do botão

    tela.blit(txt_botao2 , (largura/8+105, altura/2+207)) 


    pygame.display.update()  

def vitoria():

    global continuar


    guerreiro.hp_atual = guerreiro.hp_maximo
    vilao1.hp_atual = vilao1.hp_maximo
    arqueiro.hp_atual = arqueiro.hp_maximo
    vilao2.hp_atual = vilao2.hp_maximo


    mouse = pygame.mouse.get_pos() 
    tela.blit(jogo.bg4, (0, 0))

    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: pygame.quit()

        #coordenadas do botão    
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/3+40 <= mouse[0] <= largura/3+180 and altura/2+200 <= mouse[1] <= altura/2+240: 
                continuar = True

                   
#define a cor do botão ao interagir    
    if largura/3+40 <= mouse[0] <= largura/3+180 and altura/2+200 <= mouse[1] <= altura/2+240: 
        pygame.draw.rect(tela,cor_clara,[largura/3+40, altura/2+200,140,40]) #desenho do botão
          
    else: 
        pygame.draw.rect(tela,cor_escura,[largura/3+40,altura/2+200,140,40]) #desenho do botão
      
#posição do texto do texto
    tela.blit(txt_botao3 , (largura/3+50, altura/2+207)) 

    pygame.display.update()  

def derrota():
    global continuar
    mouse = pygame.mouse.get_pos() 
    tela.blit(jogo.bg5, (0, 0))

    guerreiro.hp_atual = guerreiro.hp_maximo
    vilao1.hp_atual = vilao1.hp_maximo
    arqueiro.hp_atual = arqueiro.hp_maximo
    vilao2.hp_atual = vilao2.hp_maximo

    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: pygame.quit()

        #coordenadas do botão    
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/3+40 <= mouse[0] <= largura/3+180 and altura/2+200 <= mouse[1] <= altura/2+240: 
                continuar = True

                   
#define a cor do botão ao interagir    
    if largura/3+40 <= mouse[0] <= largura/3+180 and altura/2+200 <= mouse[1] <= altura/2+240: 
        pygame.draw.rect(tela,cor_clara,[largura/3+40, altura/2+200,140,40]) #desenho do botão
          
    else: 
        pygame.draw.rect(tela,cor_escura,[largura/3+40,altura/2+200,140,40]) #desenho do botão
      
#posição do texto do texto
    tela.blit(txt_botao3 , (largura/3+50, altura/2+207)) 

    pygame.display.update()  

def fim():
    global continuar
    mouse = pygame.mouse.get_pos() 
    tela.blit(jogo.bg11, (0, 0))

    guerreiro.hp_atual = guerreiro.hp_maximo
    vilao1.hp_atual = vilao1.hp_maximo
    arqueiro.hp_atual = arqueiro.hp_maximo
    vilao2.hp_atual = vilao2.hp_maximo

    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: pygame.quit()

        #coordenadas do botão    
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/3+40 <= mouse[0] <= largura/3+180 and altura/2+200 <= mouse[1] <= altura/2+240: 
                continuar = True

                   
#define a cor do botão ao interagir    
    if largura/3+40 <= mouse[0] <= largura/3+180 and altura/2+200 <= mouse[1] <= altura/2+240: 
        pygame.draw.rect(tela,cor_clara,[largura/3+40, altura/2+200,140,40]) #desenho do botão
          
    else: 
        pygame.draw.rect(tela,cor_escura,[largura/3+40,altura/2+200,140,40]) #desenho do botão
      
#posição do texto do texto
    tela.blit(txt_botao3 , (largura/3+50, altura/2+207)) 

    pygame.display.update()  



while True :
    while ganhador != 1:
        if heroi_escolhido == False: 
            escolher_heroi1() #heroi 1
        
        else:
            if fase_escolhida == False:
                escolher_fase1() #heroi 1 + fase 1
        
            else:
                if ganhador == 0:
                    batalha_fase1() #heroi 1 + fase 1 + vilao1
                
                else:
                    if ganhador == 2:
                        if continuar == False:
                            derrota()
                        else:
                            pass
                            #escolher_heroi1() #fim do loop
                    

    if continuar == False:
        vitoria()
    else:
        if num_heroi == 0:
            escolher_heroi2()
        else:
            if num_heroi == 1: #heroi 1
                if num_fase == 0:
                    escolher_fase2() 
                else:
                    if num_fase == 1:
                        batalha_fase1() #fim do loop
                    else:
                        if ganhador == 0:
                            batalha_fase2_h1() #heroi 1 + fase 2 + vilao 2
                        else:
                            if ganhador == 2:
                                if continuar == False:
                                    derrota()
                                else:
                                    escolher_heroi2()
                            else:
                                if continuar == False:
                                    fim()
                                else:
                                    escolher_heroi2() #fim do loop

            else:
                if num_fase == 0:
                    escolher_fase2()
                elif num_fase == 1:
                    if ganhador == 0:
                        batalha_fase1_h2() #heroi 2 + fase 1 + vilao 1
                    elif ganhador == 2:
                        if continuar == False:
                            derrota()
                        else:
                            escolher_heroi2() #fim do loop
                    else:
                        if continuar == False:
                            vitoria()
                        else:
                            escolher_heroi2 #fim do loop


                else:
                    if ganhador == 0:
                        batalha_fase2_h2() #heroi 2 + fase 2 + vilao 2
                    else:
                        if ganhador == 2:
                            if continuar == False:
                                derrota()
                            else:
                                escolher_heroi2() #fim do loop
                        else:
                            if continuar == False:
                                fim()
                            else:
                                escolher_heroi2 #fim do loop






