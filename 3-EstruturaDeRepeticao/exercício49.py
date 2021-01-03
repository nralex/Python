##############################################################
# Faça um programa que mostre os n termos da Série a seguir: #
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.             #
##############################################################
n = int(input('Digite um número: '))
denominador = numerador = 1
print('S = ', end='')
for c in range(0, n):
    if c == n-1:
        print(f'{numerador}/{denominador}')
    if c < n-1:
        print(f'{numerador}/{denominador} + ', end='')
    denominador += 2
    numerador += 1
