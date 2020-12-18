"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será
mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(número=1, show=False):
    """
    fatorial(número=1, show=False):
        -> Calcula o fatorial de um número.
        :param n: O número a ser calculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número n.
    """
    print('-' * 30)
    f = 1
    for c in range(número, 0, -1):
        f *= c
        if show == True:
            if c == 1:
                print(c, end=' = ')
            else:
                print(c, end=' x ')
    return f


print(fatorial(5, True))
help(fatorial)