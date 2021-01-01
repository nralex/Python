# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                        Até 5 Kg           Acima de 5 Kg
#   Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#   Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a 
# quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o 
# valor a ser pago pelo cliente.
morangos = str(input('Deseja quantos quilos de morango? ')).strip().replace(',', '.')
mor = float(morangos)
maçãs = str(input('Deseja quantos quilos de morango? ')).strip().replace(',', '.')
mac = float(maçãs)
massa = mor + mac

if mor <= 5:
    preço_mor = mor * 2.5
else:
    preço_mor = mor * 2.2
if mac <= 5:
    preço_mac = mac * 1.8
else:
    preço_mac = mac * 1.5

total = preço_mac + preço_mor
if massa >= 8 or total >= 25: 
    print(f'Total: R$ {total * 0.9:.2f}')
else:
    print(f'R$ {total:.2f}')
print('-' * 42, f'\nSem desconto: {total:.2f}')
