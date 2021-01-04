#########################################################################################
# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.                 #
#########################################################################################
números = []
# quantos_números = int(input('Quantos números quer armazenar? '))
quantos_números = 5
for contador in range(1, quantos_números + 1):
    números.append(int(input(f'{contador}° n°: '))) # guarda os valores em uma lista.
for c in range(1, len(números) + 1): # mostra a lista de uma forma mais bonitinha.
    print(números[c-1], end=' ') 
