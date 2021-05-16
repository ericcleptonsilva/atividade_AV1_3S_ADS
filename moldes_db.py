import repositorio_alunos as aluno
import repositorio_disciplinas as disciplina
import repositorio_notas as notas
import consulta_tabela_disciplina_id as consult
import consulta_tabela_alunos_id as consultAluno
import random


class Alunosdb:
    def __init__(self):
        self.lista_d = []
        self.id = None
        self.cpf = aluno.RepoAlunos().gen_Cpf()
        self.nome = aluno.RepoAlunos().gen_nomesAlunos()
        self.email = aluno.RepoAlunos().gen_Email()
        self.matricula = aluno.RepoAlunos().gen_Matricula()
        self.disciplina_id = self.lista_d
        for i in range(len(self.cpf)):
            d = random.choice(consult.ConsultaTabelaDisciplina().colsutDis())
            self.lista_d.append(d)


class Disciplinasdb:
    def __init__(self):
        self.id = disciplina.RepoDisciplinas().gen_id()
        self.nome = disciplina.RepoDisciplinas().gen_nome()
        self.codigo = disciplina.RepoDisciplinas().gen_codigo()


class Notasdb:
    def __init__(self,):
        listaidalunos = consultAluno.ConsultaTabelaAlunoId().colsutDisId()
        liastaidDis = consultAluno.ConsultaTabelaAlunoId().colsutAluId()
        self.aluno_id = listaidalunos
        self.disciplina_id = liastaidDis
        self.nota_01 = notas.RepoNotas().gen_notas()
        self.nota_02 = notas.RepoNotas().gen_notas()
        self.nota_03 = notas.RepoNotas().gen_notas()
