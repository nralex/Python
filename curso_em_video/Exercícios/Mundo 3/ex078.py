''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''
n = list()
for c in range(0,5):
    n.append(int(input(f'Digite um número para aposição {c}: ')))
print('-' * 60)
print(f'Você digitou os números {n}')
maior = max(n)
menor = min(n)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for a, b in enumerate(n):
    if b == maior:
        print(f'{a}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for a, b in enumerate(n):
    if b == menor:
        print(f'{a}... ', end='')
print()
