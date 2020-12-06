'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = float(input('Insira um valor: '))
n2 = float(input('Insira um valor: '))
print('-+' * 10)
print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
print('+-' * 10)
opções = int(input('Insira uma opção: '))
while opções != 5:
    if opções == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
    if opções == 2:
        print(f'O produto entre {n1} e {n2} é {n1 * n2}.')
    if opções == 3:
        if n1 > n2:
            print(f'O maior valor entre {n1} e {n2} é {n1}.')
        else:
            print(f'O maior valor entre {n1} e {n2} é {n2}.')
    if opções > 5:
        print('Opção inválida. Tente novamente')
    if opções == 4:
        print('Insira novos valores: ')
        n1 = float(input('Insira um valor: '))
        n2 = float(input('Insira um valor: '))
    sleep(2)
    print('-+' * 10)
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    print('+-' * 10)
    opções = int(input('Insira uma opção: '))
print('Obrigado por usar os nossos serviços!')