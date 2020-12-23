def metade(n, formatado=True):
    valor = n / 2
    if formatado == False:
        return valor
    else:
        return f'R${valor:.2f}'


def dobro(n, formatado=True):
    valor = n * 2
    if formatado == False:
        return valor
    else:
        return f'R${valor:.2f}'

def aumentar(n, porcentagem, formatado=True):
    valor = n * (1 + (porcentagem / 100)) 
    if formatado == False:
        return valor
    else:
        return f'R${valor:.2f}'


def diminuir(n, porcentagem, formatado=True):
    valor = n * (1 - (porcentagem / 100)) 
    if formatado == False:
        return valor
    else:
        return f'R${valor:.2f}'


def moeda(n):
    return f'R${n:.2f}'


def resumo(n, aum, red):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'{"Preço analisado:":25}', f'{moeda(n):>14}')
    print(f'{"Dobro do preço:":25}', f'{dobro(n):>14}')
    print(f'{"Metade do preço:":25}', f'{metade(n):>14}')
    print(f'{f"{aum}% de aumento:":25}', f'{aumentar(n, aum):>14}')
    print(f'{f"{red}% de redução:":25}', f'{diminuir(n, red):>14}')
    print('-' * 40)