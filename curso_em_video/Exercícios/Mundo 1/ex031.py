distância = int(input('Qual a distância da sua viagem em km: '))
if distância <= 200:
    print(f'O preço da passagem é R${distância * (0.5):.2f}')
else:
    print(f'O preço da passagem é R${distância * (0.45):.2f}')