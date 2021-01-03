#############################################################################################
# Faça um programa que leia uma quantidade indeterminada de números positivos e conte       #
# quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].        #
# A entrada de dados deverá terminar quando for lido um número negativo.                    #
#############################################################################################
_0a25 = _26a50 = _51a75 = _76a100 = 0
números = []
while True:
    número = int(input('Digite um número [negativos para sair] '))
    números.append(número)
    if número < 0:
        break
    if 0 <= número <= 25:
        _0a25 += 1
    if 26 <= número <= 50:
        _26a50 += 1
    if 51 <= número <= 75:
        _51a75 += 1
    if 76 <= número <= 100:
        _76a100 += 1
print()
for c in range(1, len(números) + 1):
    print(números[c-1], end=' ')
print(f"""
Números por faixa:
[0-25] = {_0a25}
[26-50] = {_26a50}
[51-75] = {_51a75}
[76-100] = {_76a100}""")