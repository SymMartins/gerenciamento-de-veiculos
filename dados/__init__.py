from interface import *
import mysql.connector
from mysql.connector import Error


#  Dados dos Motoristas


def criaTabelaDadosMotorista(nome):
    try:
        #  Cria conexão com o banco de dados:
        con = mysql.connector.connect(host='localhost', database='db_ger_frotas',
                                      user='root', password='Smb@162534')

        # Declaração SQL para ser executada:
        criar_tabela_SQL = """CREATE TABLE if not exists {} (
        IdMotorista INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NUlL,
        Nome VARCHAR(100) not null,
        Endereco1 VARCHAR (100) not null,
        Endereco2  VARCHAR (100),
        Telefone VARCHAR (20) not null,
        CNH VARCHAR (20) not null);""".format(nome)

        # criar cursor e executar SQL no banco de dados:
        cursor = con.cursor()
        cursor.execute(criar_tabela_SQL)
        #  print('Tabela criada Motorista com sucesso!')

        #  Mostra o erro na criação da tabela:
    except mysql.connector.Error as erro:
        print(f'Falha ao criar tabela!')

    finally:
        #  Encerra a conexão com o banco de dados
        if con.is_connected():
            cursor.close()
            con.close()


def cadastraMotorista():
    #  Capta os dados do motorista
    while True:
        Nome = input('Nome: ').title().strip()
        End1 = input('End1: ').title().strip()
        End2 = input('End2: ').title().strip()
        Tel = input('Tel: ')
        Cnh = input('CNH: ')

        dados = '\'' + Nome + '\'' + ',\'' + End1 + '\'' + ',\'' + End2 + '\'' + ',\'' \
                + Tel + '\'' + ',\'' + Cnh + '\'' + ')'
        declaracao = """INSERT INTO tbldadosmotorista 
        (Nome, Endereco1, Endereco2, Telefone, CNH)
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
            print(f'Falha ao Cadastrar!Erro: {erro}')

        finally:
            #  Encerra a conexão com o banco de dados
            if con.is_connected():
                cursor.close()
                con.close()

        sair = str(input('Deseja cadastrar outro motorista ? [S/N]')).upper().strip()[0]
        if sair == 'N':
            break


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


def deletaMotorista(idMotorista):
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
        criar_tabela_SQL = """CREATE TABLE if not exists {} (
        IdVeiculo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
        Marca VARCHAR(100) not null,
        Modelo VARCHAR(100) not null,
        Ano_de_Fabricação VARCHAR(100) not null,
        Quilometragem VARCHAR(100) not null,
        Chassi VARCHAR (100)not null)""".format(nome)

        # criar cursor e executar SQL no banco de dados:
        cursor = con.cursor()
        cursor.execute(criar_tabela_SQL)
        #  print('Tabela de Veículos criada com sucesso!')

        #  Mostra o erro na criação da tabela:
    except mysql.connector.Error as erro:
        print(f'Falha ao criar tabela Veículos!')

    finally:
        #  Encerra a conexão com o banco de dados
        if con.is_connected():
            cursor.close()
            con.close()


def cadastraVeiculo():
    while True:
        #  Capta os dados do motorista
        Tipo = input('Tipo [Carro / Caminhão / Moto / Outro: ')
        Marca = input('Marca: ').title().strip()
        Modelo = input('Modelo: ').title().strip()
        Ano_de_Fabricacao = input('Ano de Fabricação: ')
        Quilometragem = input('Quilometragem: ')
        Chassi = input('Chassi: ')

        dados = '\'' + Tipo + '\'' + ',\'' + Marca + '\'' + ',\'' + Modelo + '\'' + ',\'' + Ano_de_Fabricacao + '\'' + \
                ',\'' + Quilometragem + '\'' + ',\'' + Chassi + '\'' + ')'
        declaracao = """INSERT INTO tbldadosveiculos 
        (Tipo, Marca, Modelo, Ano_de_Fabricação, Quilometragem, Chassi)
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
        sair = str(input('Deseja cadastrar outro Veículo ? [S/N]')).upper().strip()[0]
        if sair == 'N':
            break


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
            print('Id Veículo:', linha[0], '-', 'Tipo:', linha[1], '-', 'Marca:', linha[2],
                  '-', 'Modelo:', linha[3], '-', 'Ano de Fabricação:', linha[4],
                  '-', 'Quilometragem:', linha[5], '-', 'Chassi:', linha[6])

        #  Mostra o erro na criação da tabela:
    except Error as erro:
        print(f'Falha ao Ler tabela de Veículos! Erro: {erro}')

    finally:
        #  Encerra a conexão com o banco de dados
        if con.is_connected():
            cursor.close()
            con.close()


def deletaVeiculo(idVeiculo):
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
