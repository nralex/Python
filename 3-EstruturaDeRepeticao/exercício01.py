#########################################################################
# Faça um programa que peça uma nota, entre zero e dez.                 #
# Mostre uma mensagem caso o valor seja inválido e continue pedindo     #
# até que o usuário informe um valor válido.                            #
#########################################################################
while True:
    nota = int(input('Informe uma nota entre 0 e 10: '))
    if 1 <= nota <= 10:
        break
    else:
        print('\033[31mInforme um válor válido!\033[m')
