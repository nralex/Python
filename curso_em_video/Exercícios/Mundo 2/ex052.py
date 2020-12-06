# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Digite um numero: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[32m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {numero} foi divisível {total} vezes')
if total == 2:
    print('E por isso ele é \033[32mPRIMO\033[m!')
else:
    print('E por isso ele é \033[32mNÃE É PRIMO\033[m!')