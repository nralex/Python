#########################################################################################
# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram  #
# lidas. Imprima as consoantes.                                                         #
#########################################################################################
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = []
quantos = 10
for contador in range(1, quantos + 1):
    entrada = str(input(f'{contador} caractere: ')).lower().strip()[0]
    if entrada not in vogais:   # Guarda os caracteres que não estão na lista vogais
        consoantes.append(entrada)
print(f'Foram informadas {len(consoantes)} consoantes:')
for c in range(1, len(consoantes) + 1): # mostra a lista de uma forma mais bonitinha.
    print(consoantes[c-1], end=' ') 