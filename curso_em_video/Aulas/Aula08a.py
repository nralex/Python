#Importa o modulo matemática inteiro
#import math
#n = int(input('Digite um número: '))
#r = math.sqrt(n)
#print(f'A raiz de {n} é {r}.')

#Importa somente a funcionalidade do modulo matemática que me interessa
from math import sqrt , floor
n = int(input('Digite um número: '))
r = sqrt(n)
print(f'A raiz de {n} é {floor(r)}.')
