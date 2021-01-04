#########################################################################################
# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a            #
# multiplicação e os números.                                                           #
#########################################################################################
lista = []
quantidade = 5
for c in range(1, quantidade + 1):
    lista.append(int(input(f'Informe o {c}° número de {quantidade}: ')))
print('-' * 42, f'\nA soma dos números informados: {sum(lista)}\nO produto dos números informados: ', end='')
multi = 1
for i, v in enumerate(lista):
    if v >= 1:
        multi *= v
print(multi, '\nOs números informados foram: ', end='')
for i, v in enumerate(lista):
    print(v, end=' ')
