#####################################################################################################################
# Faça um programa para imprimir:                                                                                   #
#    1                                                                                                              #
#    2   2                                                                                                          #
#    3   3   3                                                                                                      #
#    .....                                                                                                          #
#    n   n   n   n   n   n  ... n                                                                                   #
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.     #
#####################################################################################################################
def sei_la(valor):
    for c in range(1, valor + 1):
        print(f'{c:<4}' * c)


sei_la(int(input('Imprima até: ')))