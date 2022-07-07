from interface import *
import mysql.connector
from mysql.connector import Error

#  Dados dos Motoristas


def tabelaExiste(nome):
    try: 
        con = mysql.connector.connect(host='localhost', database='db_ger_frotas', user='root', password='Smb@162534')
        testa_tabela_SQL = """SELECT TABLE_NAME FROM information_schema.tables where table_schema in (SELECT 
        DATABASE());""".format(nome.replace('\'', '\''))
        
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


def criaTabelaDadosMotorista(nome):
    try:
        #  Cria conexão com o banco de dados:
        con = mysql.connector.connect(host='localhost', database='db_ger_frotas',
                                      user='root', password='Smb@162534')

        # Declaração SQL para ser executada:
        criar_tabela_SQL = """CREATE TABLE {} (
        IdMotorista INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NUL,
        Nome VARCHAR(100) not null,
        Endereco1 VARCHAR (100) not null,
        Endereco2  VARCHAR (100),
        Telefone VARCHAR (20) not null,
        CNH INT (20) not null)""".format(nome)

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
        print('Falha ao Cadastrar!')

    finally:
        #  Encerra a conexão com o banco de dados
        if con.is_connected():
            cursor.close()
            con.close()


def lerDadosMotorista():
    try:
        #  Cria conexão com o banco de dados:
        con = mysql.connector.connect(host='localhost', database='db_ger_frotas',
                                      user='root', password='Smb@162534')

        # Declaração SQL para ser executada:
        lerdados = "select * from tbldadosmotorista"

        # criar cursor e executar SQL no banco de dados:
        cursor = con.cursor()
        cursor.execute(lerdados)
        linhas = cursor.fetchall()

        for linha in linhas:
            print('Id Motorista: ', linha[0], '-', 'Nome Motorista: ', linha[1], '-', 'Endereço 1: ', linha[2], '-',
                  'Endereço 2: ', linha[3], '-', 'Telefone: ', linha[4], '-', 'CNH: ', linha[5])

        #  Mostra o erro na criação da tabela:
    except Error as erro:
        print(f'Falha ao Ler tabela Motoristas! Erro: {erro}')

    finally:
        #  Encerra a conexão com o banco de dados
        if con.is_connected():
            cursor.close()
            con.close()
            #  print("Conexão ao MySQL foi encerrada")


def deletaMotorista():
    #  Capta o Id do Motorista a ser Deletado:
    idMotorista = input('ID do Motorista: ')

    apaga = "DELETE FROM  tbldadosmotorista WHERE idMotorista = {}".format(idMotorista)

    try:
        #  Cria conexão com o banco de dados:
        con = mysql.connector.connect(host='localhost', database='db_ger_frotas',
                                      user='root', password='Smb@162534')

        # Declaração SQL para ser executada:
        apagar_motorista = apaga

        # criar cursor e executar SQL no banco de dados:
        cursor = con.cursor()
        cursor.execute(apagar_motorista)
        con.commit()
        print('Motorista deletado com Sucesso!')

        #  Mostra o erro ao deletar motorista:
    except Error as erro:
        print(f'Falha ao deletar motorista! Erro: {erro}')

    finally:
        #  Encerra a conexão com o banco de dados
        if con.is_connected():
            cursor.close()
            con.close()

#  Dados dos Veículos


def criaTabelaDadosVeiculos(nome):
    try:
        #  Cria conexão com o banco de dados:
        con = mysql.connector.connect(host='localhost', database='db_ger_frotas',
                                      user='root', password='Smb@162534')

        # Declaração SQL para ser executada:
        criar_tabela_SQL = """CREATE TABLE {} (
        IdVeiculo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
        Marca VARCHAR(100) not null,
        Modelo VARCHAR(100) not null,
        Ano_de_Fabricação VARCHAR(100) not null,
        Quilometragem VARCHAR(100) not null,
        Chassi VARCHAR (100)not null)""".format(nome)

        # criar cursor e executar SQL no banco de dados:
        cursor = con.cursor()
        cursor.execute(criar_tabela_SQL)
        print('Tabela de Veículos criada com sucesso!')

        #  Mostra o erro na criação da tabela:
    except mysql.connector.Error as erro:
        print(f'Falha ao criar tabela Veículos! Erro: {erro}')

    finally:
        #  Encerra a conexão com o banco de dados
        if con.is_connected():
            cursor.close()
            con.close()


def cadastraVeiculo():
    #  Capta os dados do motorista
    Marca = input('Marca: ').title().strip()
    Modelo = input('Modelo: ').title().strip()
    Ano_de_Fabricacao = input('Ano de Fabricação: ')
    Quilometragem = input('Quilometragem: ')
    Chassi = input('Chassi: ')

    dados = '\'' + Marca + '\'' + ',\'' + Modelo + '\'' + ',\'' + Ano_de_Fabricacao + '\'' + \
            ',\'' + Quilometragem + '\'' + ',\'' + Chassi + '\'' + ')'
    declaracao = """INSERT INTO tbldadosveiculos 
    (Marca, Modelo, Ano_de_Fabricação, Quilometragem, Chassi)
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
        print(cursor.rowcount, 'Cadastro de Veículo Efetuado com Sucesso!')

        #  Mostra o erro na criação da tabela:
    except Error as erro:
        print(f'Falha ao Cadastrar!erro {erro}')

    finally:
        #  Encerra a conexão com o banco de dados
        if con.is_connected():
            cursor.close()
            con.close()


def lerDadosVeiculo():
    try:
        #  Cria conexão com o banco de dados:
        con = mysql.connector.connect(host='localhost', database='db_ger_frotas',
                                      user='root', password='Smb@162534')

        # Declaração SQL para ser executada:
        lerdados = "select * from tbldadosveiculos"

        # criar cursor e executar SQL no banco de dados:
        cursor = con.cursor()
        cursor.execute(lerdados)
        linhas = cursor.fetchall()

        for linha in linhas:
            print('Id Veículo: ', linha[0], '-', 'Marca: ', linha[1], '-', 'Modelo: ', linha[2], '-',
                  'Ano de Fabricação: ', linha[3], '-', 'Quilometragem: ', linha[4], '-', 'Chassi: ', linha[5])

        #  Mostra o erro na criação da tabela:
    except Error as erro:
        print(f'Falha ao Ler tabela de Veículos! Erro: {erro}')

    finally:
        #  Encerra a conexão com o banco de dados
        if con.is_connected():
            cursor.close()
            con.close()


def deletaVeiculo():
    #  Capta o Id do Motorista a ser Deletado:
    idVeiculo = input('ID do Veículo: ')

    apaga = "DELETE FROM  tbldadosveiculos WHERE idVeiculo = {}".format(idVeiculo)

    try:
        #  Cria conexão com o banco de dados:
        con = mysql.connector.connect(host='localhost', database='db_ger_frotas',
                                      user='root', password='Smb@162534')

        # Declaração SQL para ser executada:
        apagar_motorista = apaga

        # criar cursor e executar SQL no banco de dados:
        cursor = con.cursor()
        cursor.execute(apagar_motorista)
        con.commit()
        print('Veículo deletado com Sucesso!')

        #  Mostra o erro ao deletar motorista:
    except Error as erro:
        print(f'Falha ao deletar Veículo! Erro: {erro}')

    finally:
        #  Encerra a conexão com o banco de dados
        if con.is_connected():
            cursor.close()
            con.close()
