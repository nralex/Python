print('-' * 40)
print('CALCULADORA DE IMC')
print('-' * 40)
peso = int(input('Insira o seu peso: (kg) '))
altura = int(input('Insira a sua altura: (cm) '))
imc = peso / (altura/100)**2
print(f'Seu IMC é {imc:.2f} ', end='')
if imc < 18.5:
    print('está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('está no PESO IDEAL')
elif 25 <= imc < 30:
    print('está com SOBREPESO')
elif 30 <= imc < 40:
    print('está OBESO')
else:
    print('está sofrendo de OBESIDADE MORBIDA')