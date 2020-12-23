def metade(n):
    return n / 2


def dobro(n):
    return n * 2


def aumentar(n, porcentagem):

    return n * (1 + (porcentagem / 100))


def diminuir(n, porcentagem):
    return n * (1 - (porcentagem / 100))


def moeda(n):
    return f'R${n:.2f}'