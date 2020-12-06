# Tabuada
n = int(input('Insira um número: '))
print('-'*13)
print(f'A tanbuada do {n} é:')
print('-'*13)
for c in range(1, 11):
    print(f'{n:<2} x {c:>2} = {n*c}')
print('-'*13)