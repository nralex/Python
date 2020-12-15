def contador(*núm):
    print('Recebi os valores ', end='')

    for cadaValor in núm:
        print(cadaValor, end=' ')
    print(f'e são ao todo {len(núm)} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
print()

def soma(*valores):
    soma = 0
    for número in valores:
        soma += número
    print('Somando os valores', end=' ')
    for cadaValor in valores:
        print(cadaValor, end=', ')
    print(f'temos {soma}.')


soma(5, 2, 8)