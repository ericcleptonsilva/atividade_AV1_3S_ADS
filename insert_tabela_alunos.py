import servicesdb 
import moldes_db as models


class InsertTabelaAlunos:
    def __init__(self):
        self.lista = []
        try:
            # abertura de conexao e aquisição
            conn = servicesdb.ConectarDB()
            """ colcoar os valores da views do usuario"""
            alunos = models.Alunosdb()
            self.lista.append((
                alunos.cpf,
                alunos.nome,
                alunos.email,
                alunos.matricula,
                alunos.disciplina_id,
            ))
            # execução de comandos para a  criação de tabela
            sql_comando = ''' INSERT INTO alunos(cpf, nome, email, matricula, disciplina_id) 
                                        VALUES(?,?,?,?,?); '''
            conn._cursor.executemany(sql_comando, self.lista)
            # for aluno_id in alunos:
            self.alunos.id = conn._cursor.lastrowid()
            conn.commit_db()

        except conn._conexao.DatabaseError as err:

            print("Erro de banco de dados - insert tabela alunos", err)

        finally:

            # fechamento de conexão
            if conn._conexao:
                conn.close_cusros()
                conn._conexao

            print("dados inseridos  com sucesso da tabela alunos!")
