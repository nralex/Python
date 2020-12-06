print('-*'*20)
print('Analizador de triângulos')
print('-*'*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('OS seguimentos acima podem formar triângulo.')
else:
    print('Os seguimentos apresentados não pode formar tiângulo.')