from interface import *

#  Dados dos Motoristas


def dadosMotorista(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaDadosMotorista(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo!')
    else:
        print(f'O aquivo {nome} foi criado com sucesso!')


def cadastraMotorista(dadosMotorista, nome, end, tel, cnh):
    try:
        a = open(dadosMotorista, 'at')
    except:
        print(f'ERRO ao abrir o arquivo {dadosMotorista}!')
    else:
        try:
            a.write(f'nome: {nome}; end: {end}; tel: {tel}; CNH: {cnh}\n')
        except:
            print('ERRO! Ao escrever os dados!')
        else:
            print(f'O motorista: {nome} foi cadastrado.')
            a.close()


def lerDadosMotoristas(dadosMotorista):
    try:
        a = open(dadosMotorista, 'rt')
    except:
        print(f'ERRO ao ler o arquivo {dadosMotorista}')
    else:
        cabecalho('MOTORISTAS CADASTRADOS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'Nome:{dados[0]:<5} - End:{dados[1]:<5} - Tel:{dados[2]:<5} - CNH:{dados[3]:>5}')
    finally:
        a.close()

#  Dados dos veículos


def dadosVeiculos(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaDadosVeiculos(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo!')
    else:
        print(f'O aquivo {nome} foi criado com sucesso!')


def cadastraVeiculos(dadosVeiculos, marca, modelo, ano, kms):
    try:
        a = open(dadosVeiculos, 'at')
    except:
        print(f'ERRO ao abrir o arquivo {dadosVeiculos}!')
    else:
        try:
            a.write(f'{marca}; {modelo}; {ano}; {kms}\n')
        except:
            print('ERRO! Ao escrever os dados!')
        else:
            print(f'O veículo: {modelo} foi cadastrado.')
            a.close()


def lerDadosVeiculos(dadosVeiculos):
    try:
        a = open(dadosVeiculos, 'rt')
    except:
        print(f'ERRO ao ler o arquivo {dadosVeiculos}')
    else:
        cabecalho('VEÍCULOS CADASTRADOS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'Marca:{dados[0]:<5} - Modelo:{dados[1]:<5} - Ano:{dados[2]:<5} - Kms:{dados[3]:>5}')
    finally:
        a.close()
