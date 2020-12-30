# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho 
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta 
# é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta 
# a serem compradas e o preço total.
metros = float(input('Informe a área ser pintada: [m²] '))
número_de_latas = metros / 54
print(número_de_latas)
if número_de_latas != int(número_de_latas):
    nl = número_de_latas.__trunc__() + 1
    print(f'Para pintar {metros} m² será necessária a compra de {nl} lata(s) de tinta.\nAo custo de R${nl * 80:.2f}')
else:
    print(f'Para pintar {metros} m² será necessária a compra de {número_de_latas} lata(s) de tinta.\nAo custo de R${número_de_latas * 80:.2f}')