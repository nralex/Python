#Maneiras diferentes de imprimir uma variável
nome = input('Digite o seu nome: ')
print(f'É um prazer te conhecer {nome}')
print('É um prazer te conhecer {}'.format(nome))
print('É um prazer te conhecer ' + nome)
print('É um prazer te conhecer ' , nome)