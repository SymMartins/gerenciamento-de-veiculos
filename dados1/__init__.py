from interface import *
import mysql.connector
from mysql.connector import Error

#  Dados dos Motoristas


"""def tabelaExiste(nome):
    try: 
        con = mysql.connector.connect(host='localhost', database='db_ger_frotas', user='root', password='Smb@162534')
        testa_tabela_SQL = ("*3)
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'("*3).format(nome.replace('\'', '\''))
        
        cursor = con.cursor()
        cursor.execute(testa_tabela_SQL)
        print('Tabela Encontrada')
        
    except mysql.connector.Error as erro:
        print(f'falha ao pesquisar tabela! Erro: {erro}')
        
    finally:
        #  Encerra a conexão com o banco de dados
        if con.is_connected():
            cursor.close()
            con.close()
            print("Conexão ao MySQL foi encerrada")"""


def criaTabelaDadosMotorista(nome):
    try:
        #  Cria conexão com o banco de dados:
        con = mysql.connector.connect(host='localhost', database='db_ger_frotas',
                                      user='root', password='Smb@162534')

        # Declaração SQL para ser executada:
        criar_tabela_SQL = """CREATE TABLE {} (
        IdMotorista INT(11) not null,
        Nome VARCHAR(100) not null,
        Endereco1 VARCHAR (100) not null,
        Endereco2  VARCHAR (100),
        Telefone VARCHAR (20) not null,
        CNH INT (20) not null,
        PRIMARY KEY (IdMotorista))
        """.format(nome)

        # criar cursor e executar SQL no banco de dados:
        cursor = con.cursor()
        cursor.execute(criar_tabela_SQL)
        print('Tabela criada com sucesso!')

        #  Mostra o erro na criação da tabela:
    except mysql.connector.Error as erro:
        print(f'Falha ao criar tabela! Erro: {erro}')

    finally:
        #  Encerra a conexão com o banco de dados
        if con.is_connected():
            cursor.close()
            con.close()
            print("Conexão ao MySQL foi encerrada")


def cadastraMotorista():
    #  Capta os dados do motorista
    idMotorista = input('ID do Motorista: ')
    Nome = input('Nome: ').title().strip()
    End1 = input('End1: ').title().strip()
    End2 = input('End2: ').title().strip()
    Tel = input('Tel: ')
    Cnh = input('CNH: ')

    dados = idMotorista + ',\'' + Nome + '\'' + ',\'' + End1 + '\'' + ',\'' + End2 + '\'' + ',' + Tel + ',' + Cnh + ')'
    declaracao = """INSERT INTO tbldadosmotorista 
    (idMotorista, Nome, Endereco1, Endereco2, Telefone, CNH)
        VALUES ( """
    sql = declaracao + dados

    try:
        #  Cria conexão com o banco de dados:
        con = mysql.connector.connect(host='localhost', database='db_ger_frotas',
                                      user='root', password='Smb@162534')

        # Declaração SQL para ser executada:
        cadastra_dados = sql

        # criar cursor e executar SQL no banco de dados:
        cursor = con.cursor()
        cursor.execute(cadastra_dados)
        con.commit()
        print(cursor.rowcount, 'Cadastro Efetuado com sucesso!')

        #  Mostra o erro na criação da tabela:
    except Error as erro:
        print(f'Falha ao Cadastrar! Erro: {erro}')

    finally:
        #  Encerra a conexão com o banco de dados
        if con.is_connected():
            cursor.close()
            con.close()
            #  print("Conexão ao MySQL foi encerrada")
