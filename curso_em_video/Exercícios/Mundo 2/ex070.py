'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar. No final mostre:
* Qual o total gasto na compra;
* Quantos produtos custam mais de R$1000.00
* Qual é o nome do produto mais barato. '''
print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)
total = mais_de_1000 = menor = c = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).upper().strip()
    preço = float   (input('Preço: R$ '))
    total += preço
    c += 1 # Contador para separa o preduto mais barato
    if preço > 1000:
        mais_de_1000 += 1
    if c == 1 or preço < menor: # O contador serve para incluir os valores abaixo:
        menor = preço
        barato = produto
    print('-' * 30)
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    print('-' * 30)
    if opção == 'N':
        print('{:-^30}'.format('FIM DO PROGRAMA'))
        break
print(f'O total da compra foi R${total:10.2f}')
print(f'Temos {mais_de_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f} ')