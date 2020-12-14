'''Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
time = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))    
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())    
    while True:
        opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if opção in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N')
    if opção == 'N':
        break
print('-' * 50)
print('cod', end='  ')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)
while True:    
    dadosJogador = int(input('Mostrar dados de qual jogador? (999 para parar) ')) 
    if dadosJogador == 999:
        break
    if dadosJogador >= len(time):
        print(f'ERRO! Não existe jogador com código {dadosJogador}.')
    else:
        for k, v in enumerate(time):
            if k == dadosJogador:
                print(f'LEVANTAMENTO DO JOGADOR {v["nome"]}')
                for p, i in enumerate(v["gols"]):
                    print(f'Na partida {p + 1}, fez {i} gols.')
                print('-' * 50)
print('<< VOLTE SEMPRE >>')
