velocidade = int(input('Qual a velocidade do carro, km/h: '))
if velocidade > 80:
    print(f'Você foi multado!\nMulta: R${(velocidade-80)*7:.2f}')
