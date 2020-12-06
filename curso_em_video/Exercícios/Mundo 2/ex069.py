''' Crie um programa que leia a idade eo sexo de várias pessoas. A cada pessoa cadastrada o programa
deverá perguntar se  o usuário quer ou não continuar. No final mostre:
* Quantidade de pessoas tem mais de 18 anos;
* Quantos homens foram cadastrados;
* Quanta mulheres tem menos de 20 anos. '''
c_homens = c_mulheres20 = c_idade = 0
while True:
    print ('-' * 25)
    print ('{:^25}'.format('CADASTRE UMA PESSOA'))
    print ('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if idade >= 18:
        c_idade += 1
    if sexo == 'M':
        c_homens += 1
    if sexo == 'F' and idade < 20:
        c_mulheres20 += 1
    print ('-' * 25)
    continuidade = ' '
    while continuidade not in 'SN':
        continuidade = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuidade in 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {c_idade}\nAo todo temos {c_homens} homens cadastrados\nE temos {c_mulheres20} mulheres com menos de 20 anos')