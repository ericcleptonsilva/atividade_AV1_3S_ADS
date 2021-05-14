import sqlite3

class ConectarDB(object):
    def __init__(self):
        try:
            self.conexaodb = sqlite3.connect('dados02.db')
            self.cursordb = self.conexaodb.cursor()

        except sqlite3.Error:
            print('Erro ao Abrir o banco de dados')
            return False

