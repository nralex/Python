def metade(n, formatado=False):
    valor = n / 2
    return valor if formatado is False else moeda(valor)


def dobro(n, formatado=False):
    valor = n * 2
    return valor if formatado is False else moeda(valor)


def aumentar(n, porcentagem, formatado=False):
    valor = n * (1 + (porcentagem / 100)) 
    return valor if formatado is False else moeda(valor)


def diminuir(n, porcentagem, formatado=False):
    valor = n * (1 - (porcentagem / 100)) 
    return valor if formatado is False else moeda(valor)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, aum=10, red=5):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'{"Preço analisado:":25}', f'{moeda(n):>14}')
    print(f'{"Dobro do preço:":25}', f'{dobro(n, True):>14}')
    print(f'{"Metade do preço:":25}', f'{metade(n, True):>14}')
    print(f'{f"{aum}% de aumento:":25}', f'{aumentar(n, aum, True):>14}')
    print(f'{f"{red}% de redução:":25}', f'{diminuir(n, red, True):>14}')
    print('-' * 40)