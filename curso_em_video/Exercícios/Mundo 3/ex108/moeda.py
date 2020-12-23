def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumentar(n=0, porcentagem=0):

    return n * (1 + (porcentagem / 100))


def diminuir(n=0, porcentagem=0):
    return n * (1 - (porcentagem / 100))


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')