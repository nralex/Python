# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, 
# informando ao usuário nas seguintes situações:
#   *   Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#   *   Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
#   *   Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#   *   Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
from math import sqrt
print(f'{" Calculo de equação de 2° grau ":-^40}')
print(f'{"ax² + bx + c = 0 ":^40}')
while True:
    a = int(input('Informe o valor de a: '))
    if a == 0:
        print('A equação não é do segundo grau')
        break
    b = int(input('Informe o valor de b: '))
    c = int(input('Informe o valor de c: '))
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print('A equação não possui raízes reais')
        break
    if delta == 0:
        print('A equação possui apenas uma raiz real')
        print('S = {',f'{-b / (2 * a)}','}')
    if delta > 0:
        print('A equação possui duas raiz reais')
        print('S = {',f'{((b * -1) + sqrt(delta)) / (2 * a)};', f'{((b * -1) - sqrt(delta)) / (2 * a)}''}')
    break
print(delta)