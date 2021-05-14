
import drop_tabela_alunos as delete_alunos
import drop_tabela_notas as delete_notas
import drop_tabela_disciplina as delete_disciplinas


class DeleteTabelas:
    def __init__(self):
        """ Intanciando a class das tabelas deletes"""
        delete_tabela1 = delete_alunos.DeleteTabelaAlunos()
        delete_tabela2 = delete_notas.DeleteTabelaNotas()
        delete_tabela3 = delete_disciplinas.DeleteTabelaDisciplinas()
