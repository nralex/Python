"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e
passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1;
b) De 10 até 0, de 2 em 2;
c) Uma contagem personalizada.
"""
from time import sleep


def contador(a, b, c):
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    for a in range(a, b + 1):
        #sleep(1)
        print(a, end=' ')
        a += c
    print()


#contador(1, 10, 1)
contador(10, 0, 2)