
import random

class RepoAlunos:
    def __init__(self):
        
        with open("D:/ERIC/CURSOS/ESTACIO/ADS/Desenvolvimento Rápido de Aplicação em Python/atividade_AV1/nome.txt", 'r') as Nome:
            self.lista_nome = Nome.readlines()
        with open("D:/ERIC/CURSOS/ESTACIO/ADS/Desenvolvimento Rápido de Aplicação em Python/atividade_AV1/sobrenome.txt", 'r') as Sobrenome:
            self.lista_sobrenome = Sobrenome.readlines()
         
        if Nome.closed and Sobrenome.closed:
            print(f"Arquivo {Nome.name} e {Sobrenome.name} já foi fechado!")
            
    def gen_nomesAlunos(self):
        for i in range(len(self.lista_sobrenome)):
            nome = self.lista_nome[i]
            sobrenome = self.lista_sobrenome[i]
            self.nomeCompelto = f'{nome.strip()} {sobrenome.strip()}'
            return self.nomeCompelto

    def gen_Cpf(self):
        cpf1 = random.randint(1, 999)
        cpf2 = random.randint(1, 999)
        cpf3 = random.randint(1, 999)
        digito = random.randint(1, 99)
        return f'{cpf1}{cpf2}{cpf3}{digito}'

    def gen_Email(self):
        for i in range(len(self.lista_sobrenome)):
            nome = self.lista_nome[i]
            sobrenome = self.lista_sobrenome[i]
            self.email = f'{nome.strip()}{sobrenome.strip()}@gmail.com'.lower()
            return self.email

    def gen_Matricula(self):
        return random.randint(1, 9999)

