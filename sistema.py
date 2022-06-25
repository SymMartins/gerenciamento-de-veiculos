from interface import *
from dados import *
from time import sleep

dados_motorista = 'dadosmotorista.txt'
dados_veiculos = 'dadosveiculos.xml'

while True:
    resposta = menu(['Cadastrar Motoristas', 'Cadastrar Veículos', 'Motoristas Cadastrados', 'Sair do Sistema'])
    if resposta == 1:
        if not dadosMotorista(dados_motorista):
            criaDadosMotorista(dados_motorista)

        cabecalho('CADASTRO DE MOTORISTA')
        nome = str(input('Nome: ')).title().strip()
        end = str(input('End: ')).title().strip()
        tel = int(input('Tel: '))
        cnh = int(input('CNH: '))
        cadastraMotorista(dados_motorista, nome, end, tel, cnh)

    elif resposta == 2:
        while True:
            resposta = submenu(['Cadastrar Veículo', 'Veículos Cadastrados', 'Menu Principal'])
            if resposta == 1:
                if not dadosVeiculos(dados_veiculos):
                    criaDadosVeiculos(dados_veiculos)

                cabecalho('CADASTRO DE VEÍCULOS')
                marca = str(input('Marca: ')).title().strip()
                modelo = str(input('Modelo: ')).title().strip()
                ano = int(input('Ano: '))
                kms = int(input('Kms:'))
                cadastraVeiculos(dados_veiculos, marca, modelo, ano, kms)

            elif resposta == 2:
                lerDadosVeiculos(dados_veiculos)

            elif resposta == 3:
                cabecalho('Voltando ao menu principal')
                break

            else:
                print('ERRO!! Digite uma opçao válida')
            sleep(0.5)

    elif resposta == 3:
        lerDadosMotoristas(dados_motorista)

    elif resposta == 4:
        cabecalho('Saindo do sistema...')
        break
    else:
        print('ERRO!! Digite uma opção válida')
    sleep(1)
