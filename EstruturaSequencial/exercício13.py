# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#   Para homens: (72.7*h) - 58
#   Para mulheres: (62.1*h) - 44.7
altura = float(input('Informe a sua altura: [m] '))
while True:
    sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
    if sexo in 'MF':
        break
    else:
        print('\033[31mInforme uma opção válida!\033[m')
if sexo == 'M':
    print(f'O seu peso ideal é {(72.7 * altura) - 58:.2f}kg')
else:
    print(f'O seu peso ideal é {(62.1 * altura) - 44.7:.2f}kg')