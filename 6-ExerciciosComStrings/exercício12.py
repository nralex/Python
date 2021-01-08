#####################################################################################################################
# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso  #
# deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o      #
# traço separador.                                                                                                  #
#                                                                                                                   #
#       Valida e corrige número de telefone                                                                         #
#       Telefone: 461-0133                                                                                          #
#       Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.                                         #
#       Telefone corrigido sem formatação: 34610133                                                                 #
#       Telefone corrigido com formatação: 3461-0133                                                                #
#####################################################################################################################
print('Valida e corrige número de telefone ')
t = str(input('Telefone: '))
telefone = t.replace('-', '')
if len(telefone) < 9:
    print(f'Telefone possui {len(telefone)} dígitos. Vou acrescentar o digito três na frente.')
    corrigidoF = '3' + telefone
    corrigidoSF = '3' + t
    print(f'Telefone corrigido sem formatação: {corrigidoF}')
    print(f'Telefone corrigido com formatação: {corrigidoSF}')
else:
    print(f'Foratado corretaente')