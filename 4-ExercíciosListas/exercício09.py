#########################################################################################
# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma #
# dos quadrados dos elementos do vetor.                                                 #
#########################################################################################
a = []
quantidade = 10
for c in range(1, quantidade + 1):
    a.append(int(input(f'Informe o {c}° número: ')))
soma = 0
for c in range(0, len(a)):
    soma += (a[c] ** 2)
print(f'A soma do quadrado de cada número informado é: {soma}')