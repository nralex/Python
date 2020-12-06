'''v = []
for c in range(0,4):
    v.append(int(input('Digite um valor: ')))
print(v)
for c, va in enumerate(v):
    print(f'Na posição {c} encontrei {va}!')'''

a = [2, 3, 4, 7]
b = a # Cria laços (o que acontece com uma lista se repete na outra)
c = a [:] # Cria-se uma cópia, uma vez que a lista a esta fatiada.
b[2] = 4
c[2] = 6
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')