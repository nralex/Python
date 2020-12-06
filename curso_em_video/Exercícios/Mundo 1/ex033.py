n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
# O maior número é:
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f'O maior número é: {maior}')
# O menor número é:
menor = n1
if menor > n2:
    menor = n2
if menor > n3:
    menor = n3
print(f'O menor número é {menor}')