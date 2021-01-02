#########################################################################################
# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.  #
# Ex.: 5!=5.4.3.2.1=120                                                                 #
#########################################################################################
fatorial = int(input('Fatorial de: '))
fat = 1
for c in range((fatorial), 0, -1):
    fat *= c
print(f'{fatorial}! = {fat}')
