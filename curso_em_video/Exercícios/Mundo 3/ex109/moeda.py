def metade(n, formatado=False):
    valor = n / 2
    return valor if formatado is False else moeda(n)


def dobro(n, formatado):
    valor = n * 2
    return valor if formatado is False else moeda(n)


def aumentar(n, porcentagem, formatado):
    valor = n * (1 + (porcentagem / 100)) 
    return valor if formatado is False else moeda(n)


def diminuir(n, porcentagem, formatado):
    valor = n * (1 - (porcentagem / 100)) 
    return valor if formatado is False else moeda(n)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
