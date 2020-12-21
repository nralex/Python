"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função
input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

Ex: n = leiaInt('Digite um nº: ')
"""
def leiaInt(mensagem=''):
    print('\n', '-' * 30, sep='')
    while True:
        número = input(mensagem).strip()
        if número.replace('-', '', 1).isdigit(): # isnumeric()
            return int(número)
        print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')

n = leiaInt('Digite um n°: ')
print(f'Você acabou de digitar o número {n}')

