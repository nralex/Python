# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades 
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = str(input('Informe um número inteiro menor que 1000: '))
numero_com_3_caracteres = f'{numero:0>3}'   # Formata para ter 3 caracteres.
n = []
for c in range(0, 3):   # Transforma a string em uma lista.
    n.append(int(numero_com_3_caracteres[c]))
    # Informa a centena, se houver, com plural, se houver.
if n[0] != 0:
    if n[0] == 1:
        print(f'{n[0]} centena', end='')
    if n[0] > 1:
        print(f'{n[0]} centenas', end='')
    # Decide entre (e) ou (,) se houver necessidade.
if n[0] > 0:
    if n[1] > 0 and n[2] > 0:
        print(', ', end='')
    if n[1] > 0 and  n[2] == 0:
        print(' e ', end='')
    # Informa a dezena, se houver, com plural, se houver.
if n[1] != 0:
    if n[1] == 1:
        print(f'{n[1]} dezena', end='')
    if n[1] > 1:
        print(f'{n[1]} dezenas', end='')
    # Coloca o (e) se houver necessidade.
if n[2] != 0 and (n[0] > 0 or n[1] > 0):
    print(' e ', end='')
    # Informa a unidade, se houver, com plural, se houver.
if n[2] != 0:
    if n[2] == 1:
        print(f'{n[2]} unidade')
    if n[2] > 1:
        print(f'{n[2]} unidades')
