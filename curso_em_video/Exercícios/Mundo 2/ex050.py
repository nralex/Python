''' O programa que lê seis números inteiros e mostra a soma daqueles que são pares.
 E desconsidera o valor digitado quando este é impar.'''
s = 0
cont = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        cont += 1
        s = s + n
if s != 0:
    print(f'Entre os {c} valores digitados, encontrei {cont} números pares, e a soma deles é {s}.')
else:
    print('Não foi digitado nenhum número par.')
