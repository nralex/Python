#####################################################################################################################
# Faça um programa para imprimir:                                                                                   #
#     1                                                                                                             #
#     1   2                                                                                                         #
#     1   2   3                                                                                                     #
#     .....                                                                                                         #
#     1   2   3   ...  n                                                                                            #
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.       #
#####################################################################################################################
def exercício2(n):
    for c in range(1, n + 1):
        for i in range(1, c + 1):
            print(f'{i:<3} ', end='')
        print()


exercício2(int(input('Digite um número: ')))