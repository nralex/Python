"""
DESAFIO 100
Faça um programa que tenha uma lista chamada números e duas funções chamdas sorteia() e somaPar(). A
primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores PARES sorteados pela função anterior.
"""
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cadaNúmero in range(0, 5):
        sleep(0.3)
        cadaNúmero = randint(1, 10)
        lista.append(cadaNúmero)
        print(cadaNúmero, end=' ')
    sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for cadaValor in lista:
        if cadaValor % 2 == 0:
            soma += cadaValor
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = []
sorteia(números)
somaPar(números)
