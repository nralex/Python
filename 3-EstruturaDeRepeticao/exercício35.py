#############################################################################################
# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos    #
# números primos existentes entre 1 e um número inteiro informado pelo usuário.             #
#############################################################################################
for contador in range(1,(int(input('Mostras os números primos de 1 a ')))):
    n = contador
    para_comparar = [1, n]
    divisível_por = []
    for c in range(1, n + 1):
        if n % c == int():
            divisível_por.append(c)
    if divisível_por == para_comparar:
        print(f'{n} ', end='')
    elif n == 1:
        print(f'{n} ', end='')