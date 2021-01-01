# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara 
# o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça: 
#       o tipo e a quantidade de carne comprada pelo usuário
#       e gere um cupom fiscal, contendo as informações da compra: 
#           tipo e quantidade de carne, 
#           preço total, 
#           tipo de pagamento, 
#           valor do desconto
#           valor a pagar.
opções = ['File Duplo', 'Alcatra', 'Picanha'] # Coloquei para tornar a interação mais interessante
carne = int(input(f"""Qual carne deseja comprar? 
[1] File Duplo
[2] Alcatra
[3] Picanha
Informe a sua opção: """)) # Pergunta o tipo de carne
print('-' * 42)
quilos = float(input(f'Quantos quilos de {opções[carne - 1]} deseja? ')) # Pergunta a quantidade de carne
print('-' * 42)
opção_de_pagamento = str(input('Deseja pagar com o cartão Tabajara? [S/N] ')).strip().upper()[0] # Solicita a forma de pagamento
print('-' * 42)
print(f'{"Carne":.<30}:{opções[carne - 1]:>11}') # Imprime o tipo de carne
# Verifica o tipo de carne e calcula o preço total.
if carne == 1 and quilos <= 5:
    preço_total = quilos * 4.9
elif carne == 1 and quilos > 5:
    preço_total = quilos * 5.8
elif carne == 2 and quilos <= 5:
    preço_total = quilos * 5.9
elif carne == 2 and quilos > 5:
    preço_total = quilos * 6.8
elif carne == 3 and quilos <= 5:
    preço_total = quilos * 6.9
elif carne == 3 and quilos > 5:
    preço_total = quilos * 7.8
print(f'{"Preço Total":.<30}: R$ {preço_total:>7.2f}') # Imprime o preço total
if opção_de_pagamento == 'S': # Verifica a forma de pagamento e dá desconto caso possa
    desconto = preço_total * 0.05
else:
    desconto = 0
print(f'{"Desconto":.<30}: R$ {desconto:>7.2f}') # Imprime o valor do desconto
print(f'{"Total a pagar":.<30}: R$ {preço_total - desconto:>7.2f}') # Imprime o preço a pagar
print('-' * 42)
