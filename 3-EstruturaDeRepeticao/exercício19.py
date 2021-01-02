#########################################################################################
# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.         #
#########################################################################################
lista = []
c = 1
while True:
    while True:
        n = (int(input(f'Informe o {c}° valor: ')))
        if 0 <= n <= 1000:
            lista.append(n)
            break
        else:
            print('\033[31mInforme um valor entre 0 e 1000\033[m')    
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