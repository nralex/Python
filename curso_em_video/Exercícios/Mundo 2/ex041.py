from datetime import date
ano = int(input('Ano de Nascimento: '))
este_ano = date.today().year
idade = este_ano - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação MIRIM')
elif idade <= 14:
    print('Classificação INFANTIL')
elif idade <= 19:
    print('Classificação JUNIOR')
elif idade <= 25:
    print('Classificação SÊNIOR')
elif idade > 25:
    print('Classificação MASTER')
'''
até 9 anos mirim
até 14 anos infantil
até 19 anos junior
até 25 anos sênior
acima master '''