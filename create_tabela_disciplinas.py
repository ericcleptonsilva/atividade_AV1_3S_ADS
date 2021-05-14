from servicesdb import *


class CreateTabelaDisciplinas:
    def __init__(self):

        try:
            # abertura de conexao e aquisição
            conn = ConectarDB()
            # execução de comandos para a  criação de tabela
            sql_comando = ''' CREATE TABLE disciplinas(
                            id INTEGER NOT NULL,
                            nome TEXT NOT NULL,
                            codigo INTEGER NOT NULL,                                                    
                            PRIMARY KEY(codigo)
                            );
                            '''

            conn._cursor.execute(sql_comando)
            conn._conexao.commit()

        except conn._conexao.DatabaseError as err:
            print("Erro de banco de dados - disciplinas", err)
        finally:
            #fechamento de conexão
            if conn._conexao:
                conn._cursor.close()
                conn._conexao.close()
            print("Criado com sucesso tabela disciplinas!")
