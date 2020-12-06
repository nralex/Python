# Esse eu realmente só copiei, mas ainda assim adaptei muita coisa.
nome = str(input('Digite o seu nome completo: ')).strip().split()
#nome = 'Alex Nunes Rodrigues'.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))