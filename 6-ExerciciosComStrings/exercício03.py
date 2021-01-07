#####################################################################################################################
# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.                        #
#####################################################################################################################
nome = str(input('Nome: '))
for c, v in enumerate(nome):
    print(v.upper())