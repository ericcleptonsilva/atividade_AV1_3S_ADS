import repositorio_alunos as aluno
import repositorio_disciplinas as disciplina
import repositorio_notas as notas

class Alunosdb:
    def __init__(self):
        self.id = None
        self.cpf = aluno.RepoAlunos().gen_Cpf()
        self.nome = aluno.RepoAlunos().gen_nomesAlunos()
        self.email = aluno.RepoAlunos().gen_Email()
        self.matricula = aluno.RepoAlunos().gen_Matricula()
        self.disciplina_id = 0


class Disciplinasdb:
    def __init__(self):
        self.id = disciplina.RepoDisciplinas().gen_id()
        self.nome = disciplina.RepoDisciplinas().gen_nome()
        self.codigo = disciplina.RepoDisciplinas().gen_codigo()


class Notasdb:
    def __init__(self,):
        self.aluno_id = 0
        self.disciplina_id = 0
        self.nota_01 = notas.RepoNotas().gen_notas()
        self.nota_02 = notas.RepoNotas().gen_notas()
        self.nota_03 = notas.RepoNotas().gen_notas()


