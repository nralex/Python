# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

#Funcionou 

'''
n = int(input('Insira um número: '))
contador = 1
fatorial = 1
while contador <= n:
    fatorial = fatorial * contador
    contador = contador + 1
print(f'{n}! = {fatorial}')
'''

# pelo Guanabara
n = int(input('Insira um número: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1  else ' = ', end='')
    f *= c
    c -= 1
print(f)