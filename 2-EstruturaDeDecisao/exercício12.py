# Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são do Imposto de Renda, que depende 
# do salário bruto (conforme tabela abaixo) e 3% para o Sindicato 
# e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
# (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#       Desconto do IR:
#   *   Salário Bruto até 900 (inclusive) - isento
#   *   Salário Bruto até 1500 (inclusive) - desconto de 5%
#   *   Salário Bruto até 2500 (inclusive) - desconto de 10%
#   *   Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
# dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
print('-' * 42)
valorHora = float(input('Qual o valor da sua hora de trabalho? R$'))
print('-' * 42)
horasTrabalhadas = int(input('Quantas horas você trabalhou este mês? '))
print('-' * 42)
salárioBruto = valorHora * horasTrabalhadas
print(f'{"Salário Bruto":30}: R${salárioBruto:>8.2f}')


if 900 < salárioBruto <= 1500:
    iRPercentual = 0.05
elif 1500 < salárioBruto <=2500:
    iRPercentual = 0.1
elif salárioBruto > 2500:
    iRPercentual = 0.2
else:
    iRPercentual = 0
iR = salárioBruto * iRPercentual


if iRPercentual != 0:
    print(f'{f"(-) IR ({int(iRPercentual * 100)}%)":30}: R${iR:>8.2f}')
else:
    print(f'{"(-) IR (Isento)":30}: R${iR:8.2f}')

sindicato = salárioBruto * 0.03
print(f'{"(-) Sindicato (3%)":30}: R${sindicato:>8.2f}')
iNSS = salárioBruto * 0.1
print(f'{"(-) INSS (10%)":30}: R${iNSS:>8.2f}')
fGTS = salárioBruto * 0.11
print(f'{"FGTS (11%)":30}: R${fGTS:>8.2f}')
totalDosDescontos = iR + iNSS +sindicato
print(f'{"Total de descontos":30}: R${totalDosDescontos:>8.2f}')
salárioLiquido = salárioBruto - totalDosDescontos
print(f'{"Salário Liquido":30}: R${salárioLiquido:>8.2f}')
print('-' * 42)
