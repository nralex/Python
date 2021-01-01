# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
# dezenas e unidades do mesmo.
# 
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades 
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = str(input('Informe um número inteiro menor que 1000: '))
numero_com_3_caracteres = f'{numero:0>3}'
n = []
for c in range(0, 3):
    n.append(int(numero_com_3_caracteres[c]))
if n[0] != 0:
    if n[0] == 1:
        print(f'{n[0]} centena', end='')
    if n[0] > 1:
        print(f'{n[0]} centenas', end='')

if n[0] > 0:
    if n[1] > 0 and n[2] > 0:
        print(', ', end='')
    if n[1] > 0 and  n[2] == 0:
        print(' e ', end='')

if n[1] != 0:
    if n[1] == 1:
        print(f'{n[1]} dezena', end='')
    if n[1] > 1:
        print(f'{n[1]} dezenas', end='')

#if n[0] != 0 or n[1] != 0:
#    print(' e ', end='')
if n[2] != 0 and (n[0] > 0 or n[1] > 0):
    print(' e ', end='')

if n[2] != 0:
    if n[2] == 1:
        print(f'{n[2]} unidade')
    if n[2] > 1:
        print(f'{n[2]} unidades')

