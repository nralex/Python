'''
Crie um programa que simule o funcionamento de um caixa
eletrônico. No início pergunte ao usuário qual será o valor
a ser sacado (números inteiros) e o programa vai informar 
quantas cédulas de cada valor serão entregues.
'''
print('=' * 40)
print('{:^40}'.format('BANCO ALEX'))
print('=' * 40)
total = int(input('Qual valor você quer sacar? R$'))
ced = 50
tc = 0
while True:
    if total >= ced:
        total -= ced
        tc += 1
    else:
        if tc > 0:
            print(f'Total de {tc:3} cédulas de R${ced:>5.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        tc = 0
        if total == 0:
            break
print('=' *40)
print('Volte sempre ao BANCO ALEX! Tenha um bom dia!')