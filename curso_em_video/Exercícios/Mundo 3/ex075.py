# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# a) Quantas vezes apareceu o 9;
# b) Quem que posição foi digitado o primeiro valor 3;
# c) Quantos foram números pares.
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
d = int(input('Digite um número: '))
n = (a, b, c, d)
# n = (int(input('Digite um número: ')),
# int(input('Digite um número: ')),
# int(input('Digite um número: ')),
# int(input('Digite um número: ')))
print(f'Você digitou os valores: {n}')

print(f'O valor 9 apareceu {n.count(9)} vezes.')
# minha solução foi longa
'''nove = 0
for t in n:
   if t == 9:
       nove += 1
print(f'O valor 9 apareceu {nove} vezes.')'''
três = 0
for t in n:
    if t == 3:
        três += 1
if três == 0:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na posição {n.index(3)+1}')
par = 0
print('Os valores pares digitados foram ', end='')
for t in n:
    if t % 2 == 0:
        par = t
        print(par, end=' ')