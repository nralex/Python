# Faça um Programa que leia três números e mostre o maior e o menor deles.
números = []
for c in range(1, 4):
    números.append(int(input(f'Digite o {c}° número: ')))
print(f'O maior número digitado foi {max(números)} e o menor foi {min(números)}.')