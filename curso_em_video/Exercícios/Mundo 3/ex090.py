'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''
aluno = {}
aluno['nome'] = str(input('Nome: ')).title().strip()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] < 7:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Aprovado'
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["média"]}')
print(f'Situação é igual a {aluno["situação"]}')