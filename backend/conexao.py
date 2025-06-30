import os
import sqlite3

def conectar():
    caminho_pasta = os.path.join(os.path.dirname(__file__), '..', 'dados')
    os.makedirs(caminho_pasta, exist_ok=True)  # cria a pasta se não existir
    caminho_banco = os.path.join(caminho_pasta, 'clientes.db')
    caminho_banco = os.path.abspath(caminho_banco)
    print(f"Caminho do banco: {caminho_banco}")  # para verificar o caminho
    conexao = sqlite3.connect(caminho_banco)
    return conexao

def criar_tabela():
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contato (
            nome TEXT,
            endereco TEXT,
            telefone TEXT
        )
    """)
    con.commit()
    con.close()

if __name__ == "__main__":
    criar_tabela()
    print("Tabela 'contato' criada com sucesso.")