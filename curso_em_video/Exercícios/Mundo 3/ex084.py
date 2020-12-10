""" Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
pessoas = []
grupo = []
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    if len(grupo) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    grupo.append(pessoas[:])
    pessoas.clear()
    if opção in 'N':
        break
print(f'Ao todo você cadastrou {len(grupo)} pessoas')
print(f'O maior peso foi {maior}kg', end=' ')
for p in grupo:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi {menor}kg', end=' ')
for p in grupo:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')