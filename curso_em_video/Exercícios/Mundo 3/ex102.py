"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será
mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(número=1, show=False):
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