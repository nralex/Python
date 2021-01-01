# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
valor_hora = float(input('Qual o valor da sua hora de trabalho? R$'))
número_de_horas = int(input('Quantas horas você trabalhou este mês? '))
print(f'Seu salário será de R${valor_hora * número_de_horas: .2f}')
