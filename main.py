import servicesdb as db
import create_tabelas as create_tabelas
import delete_tabelas as delete_tabelas
import insert_tabelas as insert_tabelas


def main():

    """ Intanciando a class para criação do banco de dados"""
    #dbconn = db.ConectarDB()
    ''' data '''
    create_tabelas.CreateTabelas()
    # delete_tabelas.DeleteTabelas()
    #insert_tabelas.InsertTabelas()


if __name__ == '__main__':
    main()

