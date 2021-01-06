#####################################################################################################################
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.   #
#####################################################################################################################
def soma(a, b, c):
    return a + b + c

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
print(f'{n1} + {n2} + {n3} = {soma(n1, n2, n3)}')