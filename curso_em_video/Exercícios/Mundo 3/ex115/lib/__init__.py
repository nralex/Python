def leiaInt(menságem):
    while True:
        try:
            a = int(input(menságem))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            continue
        else:
            return a


def linha(tamanho=42):
    return '-' * tamanho


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1 
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc