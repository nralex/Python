#############################################################################################
# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.      #
# Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:                        #
#       Fatorial de: 5                                                                      #
#       5! =  5 . 4 . 3 . 2 . 1 = 120                                                       #
#############################################################################################
f = int(input('Fatorial de: '))
fatorial = 1
print(f'{f}! = ', end='')
for c in range(f,1,-1):
    print(f'{c} x ', end='')
    fatorial *= c
print(f'1 = {fatorial}')
