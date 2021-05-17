
class AlunosModel:
    def __init__(self):
        self.lista_d = []
        self.id = None
        self.cpf = None
        self.nome = None
        self.email = None
        self.matricula = None
        self.disciplina_id = None


class DisciplinasModel:
    def __init__(self):
        self.id = None
        self.nome = None
        self.codigo = None


class NotasModel:
    def __init__(self):
        self.aluno_id = None
        self.disciplina_id = None
        self.nota_01 = None
        self.nota_02 = None
        self.nota_03 = None
