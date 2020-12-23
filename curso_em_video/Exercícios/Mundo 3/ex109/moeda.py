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
