# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#   a)  Álcool:
#   b)  até 20 litros, desconto de 3% por litro
#   c)  acima de 20 litros, desconto de 5% por litro
#   d)  Gasolina:
#   e)  até 20 litros, desconto de 4% por litro
#   f)  acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia:
#       o número de litros vendidos, 
#       o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
#       calcule e imprima o valor a ser pago pelo cliente 
# Sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
a = g =0
litros = str(input('Quantos litros ? ')).replace(',', '.') # Aceita (,) como possibilidade para escrever os decimais
l = float(litros) # Converte as strings em números reais.
opção = str(input("""Deseja abastecer com álcool ou gasolina?
[A]-álcool
[G]-gasolina
Informe a sua opção desejada: """)).upper()
if opção == 'A':
    a = l
if opção == 'G':
    g = l
# Calcula o preço de cada combustível segundo as regras.
# Para facilitar o cálculo decidi criar duas variaveis para preço, uma para cada combustível.
if g <= 20:
    preço_g = g * 2.5 * 0.97
else:
    preço_g = g * 2.5 * 0.95
if a <= 20:
    preço_a = a * 1.9 * 0.96
else:
    preço_a = a * 1.9 * 0.94
# Sei que solicita somente um combustível e que a soma é desnecessária, 
# mas dessa forma economiza código e torna possível a implementação 
# de abastecer com mais de um tipo de combustível.
print(f'R$ {preço_a + preço_g:.2f}')
