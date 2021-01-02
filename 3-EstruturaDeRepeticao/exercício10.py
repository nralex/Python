#####################################################################################
# Faça um programa que receba dois números inteiros e gere os números inteiros que  #
# estão no intervalo compreendido por eles.                                         #
#####################################################################################
print('Imprimas os números inteiros entre')
a = int(input('Início: '))
b = int(input('Fim: '))
for c in range(a, b + 1):
    print(c, end=' ')