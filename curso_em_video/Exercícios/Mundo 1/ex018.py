from math import radians , sin , cos , tan
n = int(input('Digite um numero: '))
'''se = sin(radians(n))
co = cos(radians(n))
ta = tan(radians(n))
print(f'O seno de {n} é {se:.2f}; \nO cosseno de {n} é {co:.2f}; \nA tangente de {n} é {ta:.2f}')'''
print(f'O seno de {n} é {sin(radians(n)):.2f}; \nO cosseno de {n} é {cos(radians(n)):.2f}; \nA tangente de {n} é {tan(radians(n)):.2f}')