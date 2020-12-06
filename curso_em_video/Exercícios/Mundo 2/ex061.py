''' Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
a = int(input('Primeiro de termos: '))
r = int(input('Razão: '))
n = int(input('Quantos termos: ')) # Inclui para perguntar o número de termos
c = 0
while c != n:
    print(f'{a + (c * r)} - ', end='')
    c += 1
print('FIM')