def metade(n, formatado):
    valor = n / 2
    if formatado == True:
        return f'R${valor:.2f}'
    else:
        return valor


def dobro(n, formatado):
    valor = n * 2
    if formatado == True:
        return f'R${valor:.2f}'
    else:
        return valor

def aumentar(n, porcentagem, formatado):
    valor = n * (1 + (porcentagem / 100)) 
    if formatado == True:
        return f'R${valor:.2f}'
    else:
        return valor

def diminuir(n, porcentagem, formatado):
    valor = n * (1 - (porcentagem / 100)) 
    if formatado == True:
        return f'R${valor:.2f}'
    else:
        return valor


def moeda(n):
    return f'R${n:.2f}'
