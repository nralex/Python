'''Exercício Python 062: Melhore o DESAFIO 061, 
perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

a = int(input('Primeiro de termos: '))
r = int(input('Razão: '))
n = int(input('Quantos termos: '))# Inclui para perguntar o número de termos
c = 1
t = 0
while n != 0:
    t += n
    while c <= t:
        print(f'{a} - ', end='')
        a += r
        c += 1
    print('Pausa')
    n = int(input('Quantos termos você quer a mais? '))
print('FIM')