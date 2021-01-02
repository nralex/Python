#############################################################################################
# Os números primos possuem várias aplicações dentro da Computação, por exemplo na          #
# Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo.     #
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.  #
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
