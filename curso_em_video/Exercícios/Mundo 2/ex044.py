preço = float(input('Preço: '))
print('''Formas de pagamento:
[1] À vista (dinheiro ou cheque)
[2] À vista no cartão
[3] Parcelado em até 2X
[4] Parcelado em 3X ou mais''')
pagamento = int(input('Forma de pagamento: '))
if pagamento == 1:
    print(f'Valor final: R${preço * 0.9:.2f}')
elif pagamento == 2:
    print(f'Valor final: R${preço * 0.95:.2f}')
elif pagamento == 3:
    print(f'Valor final: R${preço:.2f}')
elif pagamento == 4:
    print(f'Valor final: R${preço * 1.2:.2f}')
else:
    print('Insira uma forma de pagamento válida.')