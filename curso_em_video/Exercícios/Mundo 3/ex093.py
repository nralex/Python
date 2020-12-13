'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
totalGols = 0
for c in range(0, partidas):
    g = int(input(f'Quantos gols na partida {c}? '))
    totalGols += g
    gols.append(g)
jogador['gols'] = gols
jogador['total'] = totalGols
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p, i in enumerate(gols):
    print(f'    => Na partida {p}, fez {i} gols.')
print(f'Foi um total de {totalGols} gols.')
