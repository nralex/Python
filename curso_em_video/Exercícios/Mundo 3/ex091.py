'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
jogos = dict()
print('Valores sorteados:')
for j in range(1, 5):
    jogos[f'jogador{j}'] = randint(1, 6)
for k, v in jogos.items():
    sleep(1)
    print(f'    O {k} tirou {v} no dado.')
print('Ranking dos jogadores:')
ranking = list()
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f'    O {i + 1}° lugar: {v[0]} com {v[1]}')