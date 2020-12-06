valor = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento?'))
prestação = valor / (anos * 12)
margem = salário * 0.3
print(f'Para pagar uma casa de R${valor:.2f} em {anos} a prestação será de R${prestação:.2f} ')
if prestação > margem:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')