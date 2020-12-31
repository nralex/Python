# Faça um Programa que leia três números e mostre-os em ordem decrescente.
n = []
for c in range(1, 4):
    n.append(int(input(f'Digite o {c}° número: ')))
n.sort()
print(n)