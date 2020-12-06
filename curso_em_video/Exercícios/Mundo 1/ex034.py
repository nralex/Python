salário = float(input('Qual é o seu salário? '))
if salário > 1250:
    print(f'Seu novo salário é R${salário*1.1:.2f}')
else:
    print(f'Seu novo salário é R${salário*1.15:.2f}')