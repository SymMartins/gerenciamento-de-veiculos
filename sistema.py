from interface import *
from dados import *
from time import sleep

dados_motorista = 'dadosmotorista.txt'

while True:
    resposta = menu(['Cadastrar Motoristas', 'Cadastrar Veículos', 'Motoristas Cadastrados', 'Veículos Cadastrados',
                     'Sair do Sistema'])
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
        cabecalho('CADASTRO DE VEÍCULOS')
    elif resposta == 3:
        lerDadosMotoristas(dados_motorista)
    elif resposta == 4:
        print('Opção 4')
    elif resposta == 5:
        cabecalho('Saindo do sistema...')
        break
    else:
        print('ERRO!! Digite uma opção válida')
    sleep(1)