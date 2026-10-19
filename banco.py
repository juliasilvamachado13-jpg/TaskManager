
import sqlite3

def conectar():
    return sqlite3.connect("tarefas.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT DEFAULT 'Pendente'
        )
    """)

    conexao.commit()
    conexao.close()
