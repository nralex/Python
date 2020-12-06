'''Escreva um programa que leia um número N inteiro qualquer 
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''
print('-' * 22)
print('SEQUêNCIA DE FIBONACCI')
print('-' * 22)
n = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
c = 3
print('\n', '~' * 22)
print(f'{t1} - {t2}', end='')
while c <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1
    print(f' - {t3}', end='')
print('\n', '~' * 22)