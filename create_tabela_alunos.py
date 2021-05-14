from servicesdb import *


class CreateTabelaAlunos:
    def __init__(self):

        try:
            # abertura de conexao e aquisição
            conn = ConectarDB()
            # execução de comandos para a  criação de tabela
            sql_comando = ''' CREATE TABLE alunos(
                            id INTEGER NOT NULL,
                            cpf INTEGER NOT NULL,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            matricula INTEGER NOT NULL,                      
                            disciplina_id INTEGER NOT NULL,                                                
                            PRIMARY KEY(id),
                            FOREIGN KEY(disciplina_id) REFERENCES disciplinas(codigo) 
                        ); '''

            conn._cursor.execute(sql_comando)
            conn._conexao.commit()

        except conn._conexao.DatabaseError as err:
            print("Erro de banco de dados - alunos", err)
        finally:
            #fechamento de conexão
            if conn._conexao:
                conn._cursor.close()
                conn._conexao.close()
            print("Criado com sucesso tabela aluno!")
