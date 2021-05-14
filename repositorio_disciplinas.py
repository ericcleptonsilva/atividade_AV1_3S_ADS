
list_disciplinas = [
    'Programação',
    'Banco de dados',
    'Computação em Nuvem'
]

list_codigo = [
    2101,
    2102,
    2103,
]

list_id = [1,2,3]

class RepoDisciplinas:
    def gen_codigo(self):
        for i in range(len(list_id)):
            self.codigo = list_codigo
            return self.codigo

    def gen_nome(self):
        for i in range(len(list_id)):
            self.nome = list_disciplinas
            return self.nome


    def gen_id(self):
        for i in range(len(list_id)):
            self.id = list_id
            return self.id


