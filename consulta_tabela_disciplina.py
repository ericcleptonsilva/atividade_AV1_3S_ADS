import servicesdb
import moldes_db


class ConsultaTabelaDisciplina:
    def consultaDbDis(self):
        lista = []
        alunos = moldes_db.Alunosdb()
        try:
            ''' abertura de conexao e aquisição'''
            conn = servicesdb.ConectarDB()
            conn.cursordb.execute(''' SELECT codigo FROM disciplinas; ''')

            conn.conexaodb.commit()
            registros = conn.cursordb.fetchall()
            for registro in registros:
                lista.append(int(registro[0]))
            return lista

        except conn.conexaodb.DatabaseError as err:

            print("Erro de banco de dados - disciplinas", err)

        finally:

            # fechamento de conexão
            if conn.conexaodb:
                conn.cursordb.close()
                conn.conexaodb.close()

        print("dados inseridos  com sucesso da tabela disciplinas!")


dados = ConsultaTabelaDisciplina()
print(dados.consultaDbDis())
