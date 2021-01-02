#####################################################################################
# Faça um programa que leia 5 números e informe o maior número.                     #
#####################################################################################
números = list()
for c in range(1, 6):
    números.append(int(input(f'Digite o {c}° número: ')))
print(f'O maior número informado foi {max(números)}')