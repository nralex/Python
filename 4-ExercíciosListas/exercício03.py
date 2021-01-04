#########################################################################################
# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.                 #
#########################################################################################
números = []
quantos_números = 4
for contador in range(1, quantos_números + 1):
    números.append(float(input(f'{contador}ª nota: ')))
print(f'A média das notas informadas é {sum(números) / len(números):.2f}')