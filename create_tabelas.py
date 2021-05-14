import create_tabela_alunos as tabela_alunos
import create_tabela_notas as tabela_notas
import create_tabela_disciplinas as tabela_disciplinas


class CreateTabelas:
    def __init__(self):
        """ Intanciando a class das tabelas Create"""
        criar_tabela1 = tabela_alunos.CreateTabelaAlunos()
        criar_tabela2 = tabela_notas.CreateTabelaNotas()
        criar_tabela3 = tabela_disciplinas.CreateTabelaDisciplinas()
