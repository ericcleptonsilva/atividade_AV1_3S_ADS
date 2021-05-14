from servicesdb import *


class DeleteTabelaDisciplinas:
    def __init__(self):

        try:
            # abertura de conexao e aquisição
            conn = ConectarDB()
            # execução de comandos para a  criação de tabela
            sql_comando = ''' DROP TABLE disciplinas;'''

            conn._cursor.execute(sql_comando)
            conn._conexao.commit()

        except conn.DatabaseError as err:
            print("Erro de banco de dados - disciplinas", err)
        finally:
            #fechamento de conexão
            if conn._conexao:
                conn._cursor.close()
                conn._conexao.close()

            print("Deletado com sucesso tabela disciplinas!")
