p = float(input('Qual o preço do produto? R$'))
d = int(input('Quantos % de desconto? '))
print(f'O produto que custava R${p:.2f}, na promoção com desconto de 5% vai custar R${p*(1-(d/100)):.2f}')