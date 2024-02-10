class Membro:
    def __init__(self, nome, num):
        self.nome = nome
        self.num = num
        self.historico = []

class Livro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.status = 'Disponível'

    def __str__(self) -> str:
        return f'Título:{self.titulo}\nAutor:{self.autor}\n'

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.membros = []

    def adcLivro(self, livro):
        self.livros.append(livro)

    def adcMembro(self, membro):
        self.membros.append(membro)

    def emprestar(self):
        
        for i in self.livros:
            print(i)
        


    # def devolver():

    # def pesquisar():

newBook = Biblioteca()

while True:
    opcao = int(input(
    '''
    Bem vindo(a) à biblioteca!

    O que deseja fazer?

    [1] Adcionar livro
    [2] Adcionar membro
    [3] Pegar livro
    [4] Devolver livro
    [5] Realizar pesquisa
    [0] Sair

    Informe o número de sua escolha:

    '''
    ))

    match opcao:
        case 1:
            titulo = input('Nome do livro:')
            autor = input('Autor do livro:')
            id = int(input('Número ID:'))                
            
            novo_livro = Livro(titulo, autor, id)
            newBook.adcLivro(novo_livro)
            # print('Livro adcionado')

  
        case 2:
            nome = input('Nome:')
            num = int(input('Número ID:'))

            pessoa = Membro(nome,num)
            membro = Biblioteca()
            membro.adcMembro(Membro)
            print('Membro adcionado')
            

        case 3:
            newBook.emprestar()

        case 4:
            pass

        case 5:
            pass

        case 0:
            print('Até a próxima!')
            break

        case _:
            print('Opção inválida!')




# Adicionar livros ao catálogo.
# Adicionar membros à biblioteca.
# Permitir empréstimo de livros por membros.
# Registrar a devolução de livros.
# Pesquisar livros por título, autor ou ID.