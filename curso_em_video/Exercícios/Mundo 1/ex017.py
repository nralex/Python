from math import hypot
coposto = int(input('Digite o comprimento do cateto oposto: '))
cadjacente = int(input('Digite o comprimento do cateto adjacente: '))
print(f'O comprimento da hipotenusa é {hypot(coposto, cadjacente):.2f}')
