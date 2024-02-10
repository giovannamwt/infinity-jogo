import pygame 
from pygame import font
import sys

pygame.init() 

class Heroi1(pygame.sprite.Sprite):
     def __init__(self, velocidade, dano):        
         self.nome = 'Guerreiro'
         self.foto = pygame.image.load(r'C:\Users\giova\OneDrive\Documentos\infinity\projeto-final-php\heroi1.png')
         self.hp_inicial = 100
         self.velocidade = velocidade
         self.dano = dano

     #def morrer(self,hp,dano):
         

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
titulo1='Escolha seu herói' 
txt_botao1 = fonte_texto_pequeno.render('escolher' , True , 1) 

#variaveis que guardam imagens
heroi1 = pygame.image.load(r'C:\Users\giova\OneDrive\Documentos\infinity\projeto-final-php\heroi1.png') 
heroi2 = pygame.image.load(r'C:\Users\giova\OneDrive\Documentos\infinity\projeto-final-php\heroi2.png') 
heroi3 = pygame.image.load(r'C:\Users\giova\OneDrive\Documentos\infinity\projeto-final-php\heroi3.png') 
vilao1 = pygame.image.load(r'C:\Users\giova\OneDrive\Documentos\infinity\projeto-final-php\vilao1.png') 
vilao2 = pygame.image.load(r'C:\Users\giova\OneDrive\Documentos\infinity\projeto-final-php\vilao2.png')
vilao3 = pygame.image.load(r'C:\Users\giova\OneDrive\Documentos\infinity\projeto-final-php\vilao3.png')
fundo1 = pygame.image.load(r'C:\Users\giova\OneDrive\Documentos\infinity\projeto-final-php\fundo1.png')




pygame.display.set_caption('JOGO DA GIOVANNA') #mensagem janela


while True :     

    tela.blit(fundo1, (0, 0))
    mouse = pygame.mouse.get_pos() 

    for evento in pygame.event.get(): #apertar no x
        if evento.type == pygame.QUIT: 
            pygame.quit() 

#coordenadas do botão    
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if largura/8+10 <= mouse[0] <= largura/8+150 and altura/2+200 <= mouse[1] <= altura/2+240: 
                pygame.quit()       
    
#define a cor do botão ao interagir    
    if largura/8+10 <= mouse[0] <= largura/8+150 and altura/2+200 <= mouse[1] <= altura/2+240: 
        pygame.draw.rect(tela,cor_clara,[largura/8+10, altura/2+200,140,40]) #desenho do botão
          
    else: 
        pygame.draw.rect(tela,cor_escura,[largura/8+10,altura/2+200,140,40]) #desenho do botão
      
    #posição do texto do texto
    tela.blit(txt_botao1 , (largura/8+30, altura/2+207)) 
    

    tela.blit(heroi1, (78, 175)) #coordenadas para exibição heroi
    fontesys=pygame.font.SysFont(fonte, 60) ##### usa a fonte padrão
    txttela = fontesys.render(titulo1, 1, (0,0,0))  ##### renderiza o texto na cor desejada
    tela.blit(txttela,(230,30)) #coordenadas do titulo


    pygame.display.update()  
             