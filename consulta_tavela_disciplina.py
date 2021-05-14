import servicesdb
from moldes_db import Notasdb


class ConsultaTabelaDisciplina:
    def __init__(self):

        try:
            ''' abertura de conexao e aquisição'''
            conn = servicesdb.ConectarDB()
            sql_comando = ''' select * from pessoa where obejeto = :Objeto;'''

            conn.cursordb.executemany(sql_comando)

            conn.conexaodb.commit()

        except conn.conexaodb.DatabaseError as err:

            print("Erro de banco de dados - disciplinas", err)

        finally:

            # fechamento de conexão
            if conn.conexaodb:
                conn.cursordb.close()
                conn.conexaodb.close()

        print("dados inseridos  com sucesso da tabela disciplinas!")
