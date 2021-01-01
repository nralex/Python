# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho 
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta 
# é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta 
# a serem compradas e o preço total.
metros = float(input('Informe a área ser pintada: [m²] '))
nl = metros / (3 * 18)
print(f'Para pintar {metros} m² será necessária a compra de:')
if nl == int(nl):
    print(f'{int(nl)} lata(s) de tinta.\nAo custo de R${int(nl) * 80:.2f}')
else:
    print(f'{int(nl) + 1} lata(s) de tinta.\nAo custo de R${(int(nl) + 1) * 80:.2f}')