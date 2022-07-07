from interface import *
from dados import *
from time import sleep

dados_motorista = 'tblDadosMotorista'
dados_veiculos = 'tblDadosVeiculos'

while True:
    resposta = menu(['Cadastrar Motoristas', 'Cadastrar Veículos', 'Sair do Sistema'])
    if resposta == 1:  # Relacionado ao cadastro de motoristas
        sleep(0.3)
        while True:
            resposta = submenuMotorista(['Cadastrar Motorista', 'Motoristas Cadastrados',
                                         'Deletar Motorista', 'Menu Principal'])
            if resposta == 1:  # Cria Tabela e Cadastra um motorista
                sleep(0.3)
                criaTabelaDadosMotorista(dados_motorista)
                cabecalho('CADASTRO DE MOTORISTA')
                cadastraMotorista()
                sleep(0.3)

            elif resposta == 2:  # Lista de motoristas cadastrados
                sleep(0.3)
                cabecalho('MOTORISTAS CADASTRADOS')
                lerDadosMotorista()
                sleep(0.3)

            elif resposta == 3:  # Deleta um motorista do cadastro
                sleep(0.3)
                while True:
                    idMotorista = input('ID do Motorista: ')
                    deletar = input('Deseja realmente DELETAR este motorista? [S/N]: ').upper().strip()[0]
                    if deletar == 'S':
                        deletaMotorista(idMotorista)
                        break
                        sleep(0.3)
                    else:
                        break
                        sleep(0.3)

            elif resposta == 4:  # Volta ao menu principal
                sleep(0.3)
                cabecalho('Voltando ao menu principal')
                break
                sleep(0.3)

            else:
                print('ERRO!! Menu não encontrado!')
                sleep(0.3)

    elif resposta == 2:  # Relacionado ao cadastro de motoristas
        sleep(0.3)
        while True:
            resposta = submenuVeiculo(['Cadastrar Veículo', 'Veículos Cadastrados',
                                       'Deletar Veículo', 'Menu Principal'])
            if resposta == 1:  # Cria a tabela e cadastra os veículos
                sleep(0.3)
                criaTabelaDadosVeiculos(dados_veiculos)
                cabecalho('CADASTRO DE VEÍCULOS')
                cadastraVeiculo()
                sleep(0.3)

            elif resposta == 2:  # Lista de Veículos cadastrados
                sleep(0.3)
                cabecalho('VEÍCULOS CADASTRADOS')
                lerDadosVeiculo()
                sleep(0.3)

            elif resposta == 3:  # Deleta Veículo cadastrado
                sleep(0.3)
                while True:
                    idVeiculo = input('ID do Veículo: ')
                    deletar = input('Deseja realmente DELETAR este veículo? [S/N]: ').upper().strip()[0]
                    if deletar == 'S':
                        deletaVeiculo(idVeiculo)
                        break
                        sleep(0.3)
                    else:
                        break
                        sleep(0.3)

            elif resposta == 4:  # Volta ao menu principal
                sleep(0.3)
                cabecalho('Voltando ao menu principal')
                break
                sleep(0.3)

            else:
                print('ERRO!! Menu não encontrado!')
            sleep(0.3)

    elif resposta == 3:  # Sai do Sistema
        sleep(0.3)
        cabecalho('Saindo do sistema...')
        break
    else:
        print('ERRO!! Menu não encontrado!')
    sleep(1)
