'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores 
únicos digitados, em ordem crescente. '''
n = list()
while True:
    nInserir = (int(input('Digite um valor: ')))
    if nInserir in n:
        print('Valor duplicado! Não posso adicionar..')
    else:
        n.append(nInserir)
        print('Adicionado com sucesso ...')
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
n.sort()
print('-+' * 30)
print(f'Você digitou os valores {n}')