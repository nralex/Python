"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep


def maior(* inteiro):
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(1)
    for n in range(0, len(inteiro)):
        print(inteiro[n], end=' ')
        sleep(0.5)
    sleep(1)
    print(f'Foram informados {len(inteiro)} valores ao todo')
    sleep(1)
    if len(inteiro) == 0:
        print(f'O maior valor informado foi 0')
    else:
        print(f'O maior valor informado foi {max(inteiro)}')
    

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()