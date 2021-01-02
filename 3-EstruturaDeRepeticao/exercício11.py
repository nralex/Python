#####################################################################################
# Altere o programa anterior para mostrar no final a soma dos números.              #
#####################################################################################
print('Imprimas os números inteiros entre')
a = int(input('Início: '))
b = int(input('Fim: '))
soma = 0
for c in range(a, b + 1):
    print(c, end=' ')
    soma += c
print(f'\nA soma dos valores é {soma} ')