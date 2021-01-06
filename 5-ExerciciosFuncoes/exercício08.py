#####################################################################################################################
# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.                   #
#####################################################################################################################
def dígitos(número):
    n = str(número)
    return len(n)


valor = int(input('Informe um número inteiro: '))
print(f'O número {valor} possui {dígitos(valor)} dígitos.')
