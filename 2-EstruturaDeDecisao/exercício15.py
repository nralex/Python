# Faça um Programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
#       Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#       Triângulo Equilátero: três lados iguais;
#       Triângulo Isósceles: quaisquer dois lados iguais;
#       Triângulo Escaleno: três lados diferentes;
a = int(input('Informe o tamanho do 1° lado: '))
b = int(input('Informe o tamanho do 2° lado: '))
c = int(input('Informe o tamanho do 3° lado: '))
if  b - c  < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('É um Triângulo', end=' ')
    if a != b != c:
        print('Escaleno!')
    elif a == c == b:
        print('Equilátero!')
    elif a == b or b == c or a ==c:
        print('Isosceles!')
else:
    print('Não é um Triângulo')

