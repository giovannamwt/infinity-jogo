import sqlite3


nome_do_arquivo = "jogo.db"
conn = sqlite3.connect(nome_do_arquivo)
cursor = conn.cursor()

# Criar a tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS personagem
                (id INTEGER PRIMARY KEY,
                nome TEXT,
                foto TEXT,
                hp_atual INTEGER,
                hp_maximo INTEGER,
                dano TEXT,
                animacao_ataque TEXT)''')

# Exemplo de dados para inserir
dados_personagem = [
    ('Guerreira', 'heroi1.png', 100, 100, '[10,15 ,20 ]', 'agua'),
    ('Arqueiro', 'heroi2.png', 130, 130, '[20, 25, 30]', 'flecha'),
    ('Morte', 'vilao1.png', 100, 100, '[10,15]', 'fogo'),
    ('Espantalho', 'vilao2.png', 130, 130, '[20,25]', 'foice')

]

# Inserir os dados na tabela
cursor.executemany('''INSERT INTO personagem
                    (nome, foto, hp_atual, hp_maximo, dano, animacao_ataque)
                    VALUES (?, ?, ?, ?, ?, ?)''', dados_personagem)

# Confirmar as alterações
conn.commit()

# Fechar a conexão
conn.close()

print(f"Banco de dados {nome_do_arquivo} criado e dados inseridos com sucesso.")
