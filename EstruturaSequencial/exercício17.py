# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
# ou em galões de 3,6 litros, que custam R$ 25,00.
#   Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#
#   *   comprar apenas latas de 18 litros;
#   *   comprar apenas galões de 3,6 litros;
#   *   misturar latas e galões, de forma que o desperdício de tinta seja menor.
#       Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

metros = float(input('Informe a área ser pintada: [m²] '))
nLatas18 = metros / 108
nLatas3_6 = metros / 21.6
print(f'Para pintar {metros} m² será necessária a compra de:')
if nLatas18 != int(nLatas18):
    nl = nLatas18.__trunc__() + 1
    print(f'{nl} lata(s) de tinta de 18L ao custo de R${nl * 80:.2f} ')
else:
    print(f'{nLatas18} lata(s) de tinta de 18L ao custo de R${nLatas18 * 80:.2f}')
print('Ou')
if nLatas3_6 != int(nLatas3_6):
    nl = nLatas3_6.__trunc__() + 1
    print(f'{nl} lata(s) de tinta de 18L ao custo de R${nl * 25:.2f}')
else:
    print(f'{nLatas3_6} lata(s) de tinta de 18L ao custo de R${nLatas3_6 * 25:.2f}')
print('Ou')