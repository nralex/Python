#####################################################################################################################
# Número por extenso.                                                                                               #
# Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.      #
#####################################################################################################################
dezena = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
unidade =  ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 
            'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
número = int(input('Digite u número: '))
if 0 < número <= 19:
    print(unidade[número - 1])
if 20 <= número <= 99:
    n = str(número)
    print(dezena[int(n[0]) - 2], end='')
    if int(n[1]) != 0:
        print(f' e {unidade[int(n[1]) - 1]}')
