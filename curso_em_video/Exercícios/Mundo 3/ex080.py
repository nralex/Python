'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
numéro = list()
for c in range(0,5):
    numéro.append(input('Digite um número: '))