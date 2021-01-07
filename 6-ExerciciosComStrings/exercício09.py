#####################################################################################################################
# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx #
# e indique se é um número válido ou inválido através da validação dos dígitos verificadores erros caracteres de    #
# formatação.                                                                                                       #
#####################################################################################################################
cpf = input('Digite o sei CPF no formato xxx.xxx.xxx-xx:\n')
if len(cpf) != 14 or '.' not in cpf[3] or '.' not in cpf[7] or '-' not in cpf[11]:
    print('O CPF indicádo não é válido.')
else:
    print('O CPF indicádo é válido.')