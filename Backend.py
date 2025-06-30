import sqlite3

class TransactionObject:
    def __init__(self, db_name='clientes.db'):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                sobrenome TEXT,
                email TEXT,
                cpf TEXT
            )
        ''')
        self.conn.commit()

    def execute(self, sql, params=(), fetch=False):
        self.cur.execute(sql, params)
        self.conn.commit()
        if fetch:
            return self.cur.fetchall()

    def __del__(self):
        self.conn.close()