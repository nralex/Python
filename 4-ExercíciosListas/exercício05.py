#########################################################################################
# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.                #
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.           #
# Imprima os três vetores.                                                              #
#########################################################################################
números = []
par = []
impar = []
# quantos = int(input('Quantos números quer armazenar? '))
quantos = 20
for contador in range(1, quantos + 1):
    números.append(int(input(f'{contador}° n°: '))) # guarda os valores em uma lista números
for c in range(1, len(números) + 1): # Verifica cada item da lista
    if números[c-1] % 2 == 0: # guarda os valores pares em uma lista par
        par.append(números[c-1])
    else: # guarda os valores impares em uma lista impar
        impar.append(números[c-1])
print(f"""Os números informados foram:
{números}
Destes são pares:
{par}
E impares:
{impar}
""")