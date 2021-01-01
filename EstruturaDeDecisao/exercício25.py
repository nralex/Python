# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#   a)  "Telefonou para a vítima?"
#   b)  "Esteve no local do crime?"
#   c)  "Mora perto da vítima?"
#   d)  "Devia para a vítima?"
#   e)  "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
investigação = 0
while True:
    telefonou = str(input('Telefonou para a vítima? [S/N] ')).strip().upper()[0]
    if telefonou in 'SN':
        if telefonou == 'S':
            investigação += 1
        break
    print('\033[31mInforme uma opção válida!\033[m')
while True:
    esteve = str(input('Esteve no local do crime? [S/N] ')).strip().upper()[0]
    if esteve in 'SN':
        if esteve == 'S':
            investigação += 1
        break
    print('\033[31mInforme uma opção válida!\033[m')
while True:
    mora = str(input('Mora perto da vítima? [S/N] ')).strip().upper()[0]
    if mora in 'SN':
        if mora == 'S':
            investigação += 1
        break
    print('\033[31mInforme uma opção válida!\033[m')
while True:
    devia = str(input('Devia para a vítima? [S/N] ')).strip().upper()[0]
    if devia in 'SN':
        if devia == 'S':
            investigação += 1
        break
    print('\033[31mInforme uma opção válida!\033[m')
while True:
    trabalhou = str(input('Já trabalhou com a vítima? [S/N] ')).strip().upper()[0]
    if trabalhou in 'SN':
        if trabalhou == 'S':
            investigação += 1
        break
    print('\033[31mInforme uma opção válida!\033[m')
if investigação < 2:
    print('Inocente')
if investigação == 2:
    print('Suspeito(a)')
if 5 > investigação > 2:
    print('Cúmplice')
if investigação == 5:
    print('Assassino(a)')
