# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.
inteiro1 = int(input('Informe um número inteiro: '))
inteiro2 = int(input('Informe mais um número inteiro: '))
real = float((input('Informe um número real: ')))
print(f"""
o produto do dobro do primeiro com metade do segundo.
(2 X {inteiro1}) X ({inteiro2} / 2) = {(2 * inteiro1) * (inteiro2 / 2)}

a soma do triplo do primeiro com o terceiro.
(3 X {inteiro1}) + {real} = {(3 * inteiro1) + real}

o terceiro elevado ao cubo.
{real}³ = {real ** 3}
    """)