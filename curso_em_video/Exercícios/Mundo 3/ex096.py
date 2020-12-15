"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
terreno retangular (largura e comprimento) e mostre a área do terreno.
"""
def area(a, b):
    print(f'A Área de um terreno {a}x{b} é de {a * b:.2f}')


print(f'{"CONTROLE DE TERRENOS":^30}')
print('-' * 30)
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
