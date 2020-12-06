# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso voce de ve mostrar, para cada palavra, quais são as vogais.
nomes = ('Alexandre', 'Eduardo', 'Henrique', 'Murilo','Theo', 'Enrico', 'Henry', 
    'Nathan', 'Thiago', 'Enzo', 'Ian', 'Thomas', 'Augusto', 'Erick', 'Isaac', 'Pietro', 'Vicente')
for nome in nomes:
    print(f'\nNo nome {nome.upper()} temos ', end='')
    for letras in nome:
        if letras in 'AEIOUaeiou':
            print(letras.lower(), end=' ')