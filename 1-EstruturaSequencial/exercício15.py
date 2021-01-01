# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
# o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#   a) salário bruto.
#   b) quanto pagou ao INSS.
#   c) quanto pagou ao sindicato.
#   d) o salário líquido.
#   e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   + Salário Bruto : R$
#   - IR (11%) : R$
#   - INSS (8%) : R$
#   - Sindicato ( 5%) : R$
#   = Salário Liquido : R$

valor_hora = float(input('Qual o valor da sua hora de trabalho? R$'))
número_de_horas = int(input('Quantas horas você trabalhou este mês? '))
salário_bruto = valor_hora * número_de_horas
inss = salário_bruto * 0.08
ir = salário_bruto * 0.11
sindicato = salário_bruto * 0.05
salário_líquido = salário_bruto - inss - ir - sindicato
print(f"""+ Salário Bruto : R${salário_bruto:.2f}
- IR (11%) : R${ir:.2f}
- INSS (8%) : R${inss:.2f}
- Sindicato (5%) : R${sindicato:.2f}
= Salário Liquido : R${salário_líquido:.2f} """)
