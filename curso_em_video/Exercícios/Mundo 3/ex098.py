"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e
passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1;
b) De 10 até 0, de 2 em 2;
c) Uma contagem personalizada.
"""
from time import sleep


def contador(início, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    sleep(2)
    if início < fim:
        contador = início
        while contador <= fim:
            print(contador, end=' ')
            sleep(0.5)
            contador += passo
        print()

    if início > fim:
        contador = início
        while contador >= fim:
            print(contador, end=' ')
            sleep(0.5)
            contador -= passo
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input(f'{"Início":8}')), int(input(f'{"Fim:":8}')), int(input(f'{"Passo:":8}')))