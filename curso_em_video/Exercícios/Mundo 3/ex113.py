"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
# Não tratei uma excessão específica, todas serão executadas por igual.

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



def leiaFloat(menságem):
    while True:
        try:
            a = float(input(menságem))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            continue
        else:
            return a



n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')

print(f'o valor inteiro digitado foi {n1} e o valor real foi {n2}')