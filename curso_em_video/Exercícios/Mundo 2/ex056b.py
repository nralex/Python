s_idade = 0
m_idade = 0
nome_homem_velho = 0
idade_homem_velho = 0
mulheres = 0
for pessoas in range (1, 5):
    print(f'------ {pessoas}ª pessoa ------')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    s_idade += idade
    m_idade = s_idade / pessoas
    if sexo == 'M' and pessoas == 1:
        nome_homem_velho = nome
        idade_homem_velho = idade
    if sexo == 'M' and idade > idade_homem_velho:
        nome_homem_velho = nome
        idade_homem_velho = idade
    if sexo == 'F' and idade < 20:
        mulheres += 1
print(f'A media  da idade do grupo é de {m_idade:.2f} anos.')
print(f'O homem mais velho têm {idade_homem_velho} anos e se chama {nome_homem_velho}.')
print(f'Ao todo são {mulheres} mulher(es) com menos de 20 anos.')
