'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas cadastradas.
B) A média de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da média.'''
pessoa = dict()
grupo = list()
somaIdade = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).title().strip()
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']
    grupo.append(pessoa.copy())
    opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while opção not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N')
        opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opção == 'N':
        break
print('-' * 45)
print(f'A)  Ao todo temos {len(grupo)} pessoas cadastradas.')
print(f'B)  A média da idade é {somaIdade / len(grupo):.2f} anos.')
print('C)  As mulheres cadastradas foram ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('D)  Lista das pessoas que estão acima da média:')
for p in grupo:
    if p['idade'] >= somaIdade / len(grupo):
        for k, i in p.items():
            print(f'{k} = {i};', end=' ')
    print()
print('< ENCERRADO >')
