"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o
nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.
"""

def ficha(nome='<DESCONHECIDO>', gols=0):
    print('-' * 30)
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


nomeJogador = str(input('Nome do Jogador: '))
golsJogador = int(input('Número de Gols: '))
ficha(nomeJogador, golsJogador)