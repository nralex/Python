'''
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado
for negativo.
'''
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*13)
    print(f'A tabuada do {n} é:')
    print('-'*13)
    for c in range(1, 11):
        print(f'{n:<2} x {c:>2} = {n*c}')
    print('-'*13)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')