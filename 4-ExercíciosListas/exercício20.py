#####################################################################################################################
# As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado        #
# alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma    #
# projeção de quanto será gasto com o pagamento deste abono.                                                        #
#       Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato     #
# laboral, chegou-se a seguinte forma de cálculo:                                                                   #
#   a. Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;                              #
#   b. O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este   #
#      valor mínimo;                                                                                                #
#   c. Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos,     #
#      impostos ou outras particularidades.                                                                         #
# Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários.           #
# Um valor de salário igual a 0 (zero) encerra a digitação.                                                         #
# Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de     #
# acordo com a regra definida acima. Ao final, o programa deverá apresentar:                                        #
#   *   O salário de cada funcionário, juntamente com o valor do abono;                                             #
#   *   O número total de funcionário processados;                                                                  #
#   *   O valor total a ser gasto com o pagamento do abono;                                                         #
#   *   O número de funcionário que receberá o valor mínimo de 100 reais;                                           #
#   *   O maior valor pago como abono;                                                                              #
# A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada  #
# execução do programa.                                                                                             #
#####################################################################################################################
print('Projeção de Gastos com Abono')
print('=' * 28)
salários = []
abonos = []
while True:
   salário = float(input('Salário: '))
   if salário == 0:
      break
   salários.append(salário)
print()
print(f'{"Salário":10}  - {"Abono":10}')
for c, v in enumerate(salários):
   if v * 0.2 >=100:
      print(f'R$ {v:8.2f} - R$ {v * 0.2:5.2f} ')
      abonos.append(v * 0.2)
   else:
      print(f'R$ {v:8.2f} - R$ 100.00 ')
      abonos.append(100)
print()
print(f'Foram processados {len(salários)} colaboradores')
print(f'Total gasto com abonos: R$ {sum(abonos):.2f} ')
print(f'Valor mínimo pago a {abonos.count(100)} colaboradores')
print(f'Maior valor de abono pago: R$ {max(abonos):.2f}')
