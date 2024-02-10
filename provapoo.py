
class Livro:
    def __init__(self, titulo, autor, editora):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora    

class Romance(Livro):
    def exibir_detalhes(self):
        return f'nº de páginas: 285\nFaixa etária: 16+'

class Biografia(Livro):
    def exibir_detalhes(self):
        return f'nº de páginas: 859\nFaixa etária: Livre'

class Infantil(Livro):
    def exibir_detalhes(self):
        return f'nº de páginas: 25\nFaixa etária: Livre'


while True:
    opcao = int(input(
    '''
Bem vindo(a) à livraria!

Que tipo de livro deseja consultar?

[1] Romance
[2] Biografia
[3] Infantil
[0] Sair

Informe o número de sua escolha:'''
    ))

    match opcao:
        case 1:
            titulo = input('Nome do livro:')
            autor = input('Autor do livro:')
            editora = input('Editora:')                
            
            novo_livro = Romance(titulo, autor, editora)
            
            print(novo_livro.exibir_detalhes())


        case 2:
            titulo = input('Nome do livro:')
            autor = input('Autor do livro:')
            editora = input('Editora:')                
            
            novo_livro = Biografia(titulo, autor, editora)
            print(novo_livro.exibir_detalhes())

            
        case 3:
            titulo = input('Nome do livro:')
            autor = input('Autor do livro:')
            editora = input('Editora:')                
            
            novo_livro = Infantil(titulo, autor, editora)
            print(novo_livro.exibir_detalhes())


        case 0:
            print('Até a próxima!')
            break

        case _:
            print('Opção inválida!')
