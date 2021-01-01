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

metros = float(input('Informe a área ser pintada: [m²] ')) * 1.1
nl18 = metros / (6 * 18)
nl3 = metros / (6 * 3.6)
print(f'Para pintar {metros:.1f} m² será necessária a compra de:')
print('~' * 50)

if nl18 == int(nl18):
    print(f'{int(nl18)} lata(s) de tinta de 18 L.\nAo custo de R${int(nl18) * 80:.2f}')
else:
    print(f'{int(nl18) + 1} lata(s) de tinta de 18 L.\nAo custo de R${(int(nl18) + 1) * 80:.2f}')
print(f'{" OU ":~^50}')

if nl3 == int(nl3):
    print(f'{int(nl3)} lata(s) de tinta de 3,6 L.\nAo custo de R${int(nl3) * 25:.2f}')
else:
    print(f'{int(nl3) + 1} lata(s) de tinta de 3,6 L.\nAo custo de R${(int(nl3) + 1) * 25:.2f}')
print(f'{" OU ":~^50}')

latas18 = latas3 = 0
while True:
    if metros > 6 * 18:
        latas18 += 1
        metros -= 6 * 18
    elif metros > 6 * 3.6:
        latas3 += 1
        metros -= 6 * 18
    elif metros == 0:
        print(f'{latas18} lata(s) de tinta de 18 L;')
        print(f'{latas3} lata(s) de tinta de 3.6 L;')
        break
    elif metros != 0:        
        latas3 += 1
        print(f'{latas18} lata(s) de tinta de 18 L;')
        print(f'{latas3} lata(s) de tinta de 3.6 L;')
        break
        

print(f'Ao custo de R${(latas18 * 80) + (latas3 * 25):.2f}')
print('~' * 50)
