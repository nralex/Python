'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date
trabalhador = dict()
while True:
    trabalhador['nome'] = str(input('Nome: ')).title().strip()
    anodeNascimento = int(input('Ano de nascimento: '))
    idade = date.today().year - anodeNascimento
    trabalhador['idade'] = idade
    trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não têm): '))
    if trabalhador['ctps'] == 0:
        break
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = (trabalhador['contratação'] - anodeNascimento) + 35
    break
print('-' * 45)
for k, v in trabalhador.items():
    print(f'    -{k} tem o valor {v}')
print('-' * 45)