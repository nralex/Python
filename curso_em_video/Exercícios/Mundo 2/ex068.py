'''
FAça um programa que jogue par ou impar com o computador.
O jogo será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele 
conquistou no final do jogo.
'''
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
c = 0
while True:
    print('=-' * 15)
    nu = int(input('Diga um valor: '))
    opção = str(input('Par ou Impar? [P/I] ')).upper().strip()
    if opção == 'P':
        opção = 'DEU PAR'
    else:
        opção = 'DEU IMPAR'
    from random import randint
    nc = randint(1, 5)
    soma = nu + nc 
    if soma % 2 == 0:
        o_numero_é = 'DEU PAR'
    else:
        o_numero_é = 'DEU IMPAR'
    print('-' * 30)
    print(f'Você jogou {nu} e o computador {nc}. Total de {nu + nc} {o_numero_é}')
    print('-' * 30)
    if opção == o_numero_é:
        print('Você VENCEU!\nVamos jogar novamente...')
    else:
        break
    c += 1
print('Você PERDEU!')
print('=-' * 15)
print(f'GAME OVER! Você venceu {c} vezes.')