#############################################################################################
# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro         #
# fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele     #
# executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e    #
# o número de testes (divisões) executados.                                                 #
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