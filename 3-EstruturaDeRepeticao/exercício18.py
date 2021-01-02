#########################################################################################
# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior #
# valor e a soma dos valores.                                                           #
#########################################################################################
lista = []
c = 1
while True:
    lista.append(int(input(f'Informe o {c}° valor: ')))
    c += 1
    while True:
        opção = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
        if opção not in 'SN':
            print('\033[31mInforme uma opção válida\033[m')
        else:
            break
    if opção == 'N':
            break
print(f'O maior valor informado foi {max(lista)} e a soma de todos os valores informados é {sum(lista)} ')