'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
print('Sou seu computador...\nAcabei de pensar em um número entre 0 a 10.\nSerá que você consegue adivinhar qual foi?')
from random import randint
eu = int(input('Qual é o seu palpite? '))
computador = randint(0, 10)
cont = 1
while eu != computador:
    cont += 1
    if  eu > computador:
        print ('Menos... Tente novamente!')
        eu = int(input('Qual é o seu palpite? '))
    else:
        print ('Mais... Tente novamente!')
        eu = int(input('Qual é o seu palpite? '))
    
print(f'Acertou com {cont} tentativas, Parabéns!')
