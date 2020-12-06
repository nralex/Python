#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.
maior = 0
menor = 0
for pessoas in range (1,6):
    peso = int(input(f'Insira o peso da {pessoas}ª: kg '))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}kg')
print(f'O menor peso foi {menor}kg')


