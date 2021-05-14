import random

n = 20
arquivo = open("Lista_de_Nomes.txt", 'w')
nomesL = list()

with open('Nome.txt', 'r') as Nome:
    lista_nome = Nome.readlines()

with open('Sobrenome.txt', 'r') as Sobrenome:
    lista_sobrenome = Sobrenome.readlines()
for i in range(n):
    nome = lista_nome[i]
    sobrenome = lista_sobrenome[i]
    cpf = random.randint(1, 100)

    # receber nomes linha por linha
    nome_completo = 'Nome: {} {}, idade: {} anos'.format(
        nome.strip(), sobrenome.strip(), cpf)
    print(nome_completo)
    # adicionas as strings na lista nomesL
    nomesL.append(nome_completo)
arquivo.writelines(nomesL)

arquivo_2 = open("arquivo_01.txt", 'a')


if Nome.closed and Sobrenome.closed:
    print()
    print(f"Arquivo {Nome.name} e {Sobrenome.name} já foi fechado!")
