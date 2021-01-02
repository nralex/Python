#############################################################################################
# Faça um programa que calcule o mostre a média aritmética de N notas.                      #
#############################################################################################
quantas_notas = int(input('Quer calcular a média de quantos números: '))
notas = []
contador = 1
while True:
    notas.append(float(input(f'Informe a {contador}ª nota: ')))
    if contador == quantas_notas:
        break
    contador += 1
print(f'A média dor números apresentados é {sum(notas) / quantas_notas:.1f}') # Poderia ser {sum(notas) / len(notas)}
