"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o
nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.
"""
def ficha(nomeJogador='<DESCONHECIDO>', golsMarcados=0):
    print(f'O jogador {nomeJogador} fez {golsMarcados} gols no campeonato.')


nome = str(input('Nome do Jogador: ')).upper()
gols = str(input('Numero de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(golsMarcados=gols)
else:
    ficha(nome, gols)
