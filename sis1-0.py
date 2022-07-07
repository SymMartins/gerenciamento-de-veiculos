from interface import *
from dados import *
from time import sleep

dados_motorista = 'tblDadosMotorista'
dados_veiculos = 'tblDadosVeiculos'

while True:
    resposta = menu(['Cadastrar Motoristas', 'Cadastrar Veículos', 'Sair do Sistema'])
    if resposta == 1:
        while True:
            resposta = submenuMotorista(['Cadastrar Motorista', 'Motoristas Cadastrados',
                                         'Deletar Motorista', 'Menu Principal'])
            if resposta == 1:  # Cria Tabela e Cadastra um motorista
                criaTabelaDadosMotorista(dados_motorista)
                cabecalho('CADASTRO DE MOTORISTA')
                cadastraMotorista()

            elif resposta == 2:  # Lista de motoristas cadastrados
                cabecalho('MOTORISTAS CADASTRADOS')
                lerDadosMotorista()

            elif resposta == 3:  # Deleta um motorista do cadastro
                deletaMotorista()

            elif resposta == 4:  # Volta ao menu principal
                cabecalho('Voltando ao menu principal')
                break

            else:
                print('ERRO!! Digite uma opçao válida')
                sleep(0.5)

    elif resposta == 2:
        while True:
            resposta = submenuVeiculo(['Cadastrar Veículo', 'Veículos Cadastrados',
                                       'Deletar Veículo', 'Menu Principal'])
            if resposta == 1:  # Cria a tabela e cadastra os veículos
                criaTabelaDadosVeiculos(dados_veiculos)
                cabecalho('CADASTRO DE VEÍCULOS')
                cadastraVeiculo()

            elif resposta == 2:  # Lista de Veículos cadastrados
                lerDadosVeiculo()

            elif resposta == 3:  # Deleta Veículo cadastrado
                deletaVeiculo()

            elif resposta == 4:  # Volta ao menu principal
                cabecalho('Voltando ao menu principal')
                break

            else:
                print('ERRO!! Digite uma opçao válida')
            sleep(0.5)

    elif resposta == 3:
        cabecalho('Saindo do sistema...')
        break
    else:
        print('ERRO!! Digite uma opção válida')
    sleep(1)
