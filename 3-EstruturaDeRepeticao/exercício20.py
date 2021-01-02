#########################################################################################
# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial   #
# várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.    #
#########################################################################################
while True:
    while True:
        fatorial = int(input('Fatorial de: '))
        if 16 > fatorial > 0:
            break
        else:
            print('\033[31mInforme um números inteiros positivo e menore que 16\033[m')
    fat = 1
    for c in range((fatorial), 0, -1):
        fat *= c
    print(f'{fatorial}! = {fat}')
    
    while True:
        opção = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
        if opção not in 'SN':
            print('\033[31mInforme uma opção válida\033[m')
        else:
            break
    if opção == 'N':
            break