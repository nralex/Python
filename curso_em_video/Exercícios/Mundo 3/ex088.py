"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import sample
from time import sleep
jogos = []
jogo = []
print('-' * 45)
print(f'{" JOGA NA MEGA SENA ":+^45}')
print('-' * 45)
nJogos = int(input('Quantos jogos você quer que eu sorteie?  '))
print(f'{f"< SORTEANDO {nJogos} JOGOS >":-^45}')
for j in range(1, nJogos + 1):
    jogo = sample(range(1, 60), 6)
    jogo.sort()
    sleep(1)
    print(f'Jogo {j}: {jogo}')
    jogos.append(jogo[:])
    jogo.clear()
sleep(1)
print(f'{"< BOA SORTE! >":-^45}')
