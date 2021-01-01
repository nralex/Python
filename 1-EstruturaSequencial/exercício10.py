# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# C = 5 * ((F-32) / 9).
c = int(input('Informe a temperatura em Celsius: '))
print(f'{c}°C equivalem a {32 + ((c / 5) * 9):.2f}°F')