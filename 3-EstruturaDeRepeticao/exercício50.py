#####################################################################################################
# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos. #
#####################################################################################################
n = int(input('Digite um número: '))
print('H = ', end='')
for c in range(1, n + 1):
    if c == 1:
        print(f'1 + ', end='')
    if c < n-1:
        print(f'1/{c+1} + ', end='')
    if c == n:
        print(f'1/{c}')
print(f'Resultado: 1/{c}')

