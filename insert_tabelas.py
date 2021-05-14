from sqlite3.dbapi2 import connect
import insert_tabela_alunos as tabelas_alunos
import insert_tabela_notas as tabelas_notas
import insert_tabela_disciplina as tabelas_disciplina



class InsertTabelas:
    def __init__(self):
        ''' Inserir dados na tebelas'''
        #self.insert_alunos = tabelas_alunos.InsertTabelaAlunos()
        self.insert_notas = tabelas_notas.InsertTabelaNotas()
        #self.insert_disciplina = tabelas_disciplina.InsertTabelaDisciplina()
