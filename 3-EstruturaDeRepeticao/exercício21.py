#############################################################################################
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.  #
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.                   #
#############################################################################################
n = int(input('Digite um número: '))
para_comparar = [1, n]
divisível_por = []
for c in range(1, n + 1):
    if n % c == int():
        divisível_por.append(c)
if divisível_por == para_comparar:
    print(f'{n} é um número primo.')
elif n == 1:
    print(f'{n} é um número primo.')
else:
    print(f'{n} não é um número primo.')
