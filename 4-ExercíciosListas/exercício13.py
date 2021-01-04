#########################################################################################
# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em   #
# uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as        #
# temperaturas acima da média anual, e em que mês elas ocorreram                        #
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )                       #
#########################################################################################
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
temperaturas = []
for c in range(0, len(meses)):
    temperaturas.append(float(input(f'Média de {meses[c]}: [°C] ')))
print('As tem peraturas acima da média e o mês em que ocorreu:')
média = (sum(temperaturas) / len(temperaturas))
for c in range(0, len(temperaturas)):
    if temperaturas[c] > média:
        print(temperaturas[c], end='°C em ')
        print(meses[c])