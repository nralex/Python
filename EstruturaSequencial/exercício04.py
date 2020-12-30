# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = list()
número_de_notas = int(input('Quantas notas deseja inserir? ')) # incrementei para que calcule a amédia da quantidade de números que for solicitada
for contador in range(1, número_de_notas + 1):
    notas.append(float(input(f'Digite a {contador}ª nota: ')))
print(f'A média das notas é {sum(notas) / len(notas): .2f}')
