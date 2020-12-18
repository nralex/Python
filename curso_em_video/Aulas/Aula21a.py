def fatorial(número = 1):
    f = 1
    for c in range(número, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')