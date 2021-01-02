#####################################################################################
# Faça um programa que peça dois números, base e expoente, calcule e mostre o       #
# primeiro número elevado ao segundo número. Não utilize a função de potência       #
# da linguagem.                                                                     #
#####################################################################################

# Não compreendi bem o enunciado mas apresento duas possíveis soluções

base = int(input('Informe a base da exponenciação: '))
expoente = int(input('Informe o expoente da exponenciação: '))
print(f'{base}^{expoente} = {base ** expoente} ')
# Creio que esta seja a solução esperada
total = 1
for c in range(1, expoente + 1):
    total *= base
print(f'{base}^{expoente} = {total} ')