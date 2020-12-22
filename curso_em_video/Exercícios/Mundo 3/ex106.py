"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores.
"""
from time import sleep
c = ('\033[m',          # 0 - Sem cor
    '\033[0;30;41m',    # 1 - Vermelho
    '\033[0;30;42m',    # 2 - Verde
    '\033[0,30,43m',    # 3 - Amarelo
    '\033[0,30,44m',    # 4 - Azul
    '\033[0,30,45m',    # 5 - Roxo
    '\033[7;30m'        # 6 - Branco
    )


def título(menságem, cor=0):
    tamanho = len(menságem) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {menságem}')
    print('~' * tamanho)
    print(c[0], end='')
    sleep(1)


def ajuda(com):
    título(f'Acessando a manual do comando \'{com}\'', 4)
    help(com)        


comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        título('ATÉ LOGO!', 1)
        break
    else:
        ajuda(comando)
