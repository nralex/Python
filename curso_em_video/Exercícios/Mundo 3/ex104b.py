"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função
input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

Ex: n = leiaInt('Digite um nº: ')
"""
def leiaInt(menságem):
    inteiro = False
    valor = 0
    while True:
        número = str(input(menságem))
        if número.isnumeric():
            valor = int(número)
            inteiro = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if inteiro:
            break
    return valor


n = leiaInt('Digite um n°: ')
print(f'Você acabou de digitar o número {n}')