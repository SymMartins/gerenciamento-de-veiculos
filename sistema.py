from interface import *
from dados import *
dados_motorista = 'dadosmotorista.txt'

"""if not dadosMotorista(dados_motorista):
    criarArquivo(dados_motorista)"""

while True:
    resposta = menu(['Cadastrar Motoristas', 'Cadastrar Veículos', 'Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Opção 3')
        break
    else:
        print('ERRO!! Digite uma opção válida')


