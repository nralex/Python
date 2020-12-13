jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for p, i in enumerate(gols):
    print(f'    => Na partida {p}, fez {i} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
