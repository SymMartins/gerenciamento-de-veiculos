def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO!! Somente números inteiros são permitidos!')
            continue
        except (KeyboardInterrupt):
            print('ERRO!! Usuário não digitou o número!')
            return 0
        else:
            return n


def lin(tam=42):
    return '=' * tam


def cabecalho(txt):
    print(lin())
    print(txt.center(42))
    print(lin())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(lin())
    opc = leiaInt('Sua Opção: ')
    return opc
