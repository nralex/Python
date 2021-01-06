#####################################################################################################################
# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721. #
#####################################################################################################################

def reverso(número):
    n = str(número)
    return n[::-1]


valor = int(input('Digite um número: '))
print(f'{valor} -> {reverso(valor)}')