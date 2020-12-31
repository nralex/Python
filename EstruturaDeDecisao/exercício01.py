# Faça um Programa que peça dois números e imprima o maior deles.
números = []
for c in range(1, 3):
    números.append(int(input(f'Digite o {c}° número: ')))
print(f'O maior número digitado foi {max(números)}')