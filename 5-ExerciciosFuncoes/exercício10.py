#####################################################################################################################
# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor #
# entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na #
# primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,#
# este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde,  #
# no entanto, se tirar um 7 antes de tirar este Ponto novamente.                                                    #
#####################################################################################################################
def craps():
    from random import randint
    from time import sleep
    dado = randint(2, 12)
    print(dado)
    sleep(1)
    if dado == 7 or dado == 11:
        print('Você um natural e ganhou')
    elif dado == 2 or dado == 3 or dado == 12:
        print('Craps e você perdeu')
    elif dado == 4 or dado == 5 or dado == 6 or dado == 8 or dado == 9 or dado == 10:
        ponto = dado
        while True:
            sleep(1)
            p = randint(2, 12)
            print(p)
            if p == ponto:
                print('Você ganhou!')
                break
            elif p == 7:
                print('Você perdeu!')
                break


craps()