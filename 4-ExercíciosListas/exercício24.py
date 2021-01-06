#####################################################################################################################
# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.  #
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para   #
# gerar numeros aleatórios, simulando os lançamentos dos dados.                                                     #
#####################################################################################################################
from random import randint
lançamentos = 100
faces = 6
resultados = []
print(f'Lancei o dado {lançamentos} vezes e:')
for c in range(0, lançamentos):
    resultados.append(randint(1, faces))
for c in range(1, faces + 1):
    print(f'o n° {c} apareceu {resultados.count(c)} vezes')
    