#########################################################################################
# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.  #
#########################################################################################
números = []
quantos_números = 10
for contador in range(1, quantos_números + 1):
    números.insert(0, int(input(f'{contador}° n°: '))) # guarda os valores na posição [0] assim ao mostrar a lista esta já estará invertida.
for c in range(1, len(números) + 1):  # mostra a lista de uma forma mais bonitinha.
    print(números[c-1], end=' ')
