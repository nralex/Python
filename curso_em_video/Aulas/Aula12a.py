nome = str(input('Qual é o seu nome? '))
if nome == 'Alex':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Doralice Barbara Isabel':
    print('Belo nome feminino!')
else:
    print('SEu noe é bem normal!')
print(f'Tenha um bom dia, {nome}!')