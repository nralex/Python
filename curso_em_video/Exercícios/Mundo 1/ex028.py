from random import randint
n = int(input('Estou pensando em um número de 0 a 5, qual é? '))
nrand = randint(0,5)
if n == nrand:
    print('Você acertou!')
else:
    print(f'Que pena você errou!\nEu estava pensando no número {nrand}.')