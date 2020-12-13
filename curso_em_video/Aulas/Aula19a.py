pessoas = {'nome': 'Alex', 'sexo': 'M', 'idade': 35}
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(f'O {pessoas ["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
del pessoas['sexo']
pessoas['nome'] = 'Laura'
pessoas['idade'] = 2
pessoas['peso'] = 13
for k, v in pessoas.items():
    print(f'{k} = {v}')