'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''
from datetime import date
este_ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Ano de nascimento da {c}ª pessoa:'))
    if este_ano - ano < 18:
        menor += 1
    else:
        maior += 1
print(f'A partir das datas inseridas {menor} pessoas não atingiram a maioridade, e {maior} pessoas atingiram a maioridade.')