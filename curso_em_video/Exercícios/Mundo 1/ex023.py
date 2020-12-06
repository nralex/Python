n = input('Digite um númer de 0 a 9999: ')
n2 = n.rjust(4)
n1 = list(n2)
# unidades
print(f'unidade: {n1[3]}')
# dezenas
print(f'dezena: {n1[2]}')
# centenas
print(f'centena: {n1[1]}')
# milhares
print(f'milhar: {n1[0]}')