#####################################################################################
# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de   #
# números pares e a quantidade de números impares.                                  #
#####################################################################################
par = 0
impar = 0
for c in range(1, 11):
    valor = int(input(f'Informe o {c}° valor: '))
    if valor % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Foram informados {par} número(s) par(es) e {impar} número(s) impar(es)')