from interface import *
from dados1 import *
from time import sleep

dados_motorista = 'tblDadosMotorista'

while True:
    resposta = menu(['Cadastrar Motoristas', 'Cadastrar Veículos', 'Sair do Sistema'])
    if resposta == 1:
        while True:
            resposta = submenuMotorista(['Cadastrar Motorista', 'Motoristas Cadastrados',
                                         'Deletar Motorista', 'Menu Principal'])
            if resposta == 1:  # Cadastra Motorista
                #  if not tabelaExiste(dados_motorista):
                criaTabelaDadosMotorista(dados_motorista)
                cabecalho('CADASTRO DE MOTORISTA')
                cadastraMotorista()

            elif resposta == 2:  # Ler os dados dos motoristas
                pass

            elif resposta == 3:  # Deletar um motorista do cadastro
                pass

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
            if resposta == 1:
                pass

            elif resposta == 2:
                pass

            elif resposta == 3:
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
