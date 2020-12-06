#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo
# Qual o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos.
soma_idade = 0
idade_homem = 0
nome_homem = ''
numero_mulheres = 0
for pessoa in range(1,5):
    print(f'------- {pessoa}ª PESSOA -------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = int(input('Sexo M=1; F=2: '))
    soma_idade += idade
    media_idade = soma_idade / pessoa
    if pessoa == 1 and sexo == 1:
        idade_homem = idade
        nome_homem = nome
    if sexo == 1 and idade > idade_homem:
        idade_homem = idade
        nome_homem = nome
    if sexo == 2 and idade < 20:
        numero_mulheres = numero_mulheres + 1
print(f'A media  da idade do grupo é de {media_idade:.2f} anos.')
print(f'O homem mais velho têm {idade_homem} anos e se chama {nome_homem}.')
print(f'Ao todo são {numero_mulheres} mulher(es) con menos de 20 anos.')