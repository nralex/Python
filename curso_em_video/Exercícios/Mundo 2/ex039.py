from datetime import date
print('''INFORME O SEU SEXO:
[1] Masculino
[2] Feminino''')
gênero = int(input('Informe o seu sexo: '))
ano = int(input('Ano de nascimento: '))
este_ano = date.today().year
idade = este_ano - ano
print(f'Quem nasceu em {ano} tem {idade} anos de idade em {este_ano}.')
if gênero == 1:    
    if idade < 18:
        print(f'Ainda faltam {18 - idade} anos para o alistamento')
        print(f'Seu alistameto será em {este_ano + (18 - idade)}')
    elif idade > 18:
        print(f'Você ja deveria ter se alistado a {idade - 18} anos')    
        print(f'Seu alistamento foi em {este_ano - (idade - 18)}')
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Entretanto o seu alistamento não é obrigatório')