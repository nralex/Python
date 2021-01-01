#################################################################
# Faça um programa que leia e valide as seguintes informações:  #
#   a)  Nome: maior que 3 caracteres;                           #
#   b)  Idade: entre 0 e 150;                                   #
#   c)  Salário: maior que zero;                                #
#   d)  Sexo: 'f' ou 'm';                                       #
#   e)  Estado Civil: 's', 'c', 'v', 'd';                       #
#################################################################
while True:
    nome = str(input('Nome: (maior que 3 caracteres) ')).upper()
    if len(nome) > 3:        
        break
    print('\033[31mERRO! O nome deve possuir mais que 3 caracteres.\033[m')
while True:
    idade = int(input('Idade: (entre 0 e 150) '))
    if 0 < idade < 150:
        break
    print('\033[31mERRO! A idade deve conter no intervalo entre 0 e 150.\033[m')
while True:
    salário = float(input('Salário: (maior que zero) R$'))
    if salário > 0:
        break
    print('\033[31mERRO! Salário deve ser maior que 0.\033[m')
while True:
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if sexo in 'MF':
        break
    print('\033[31mERRO! Informe uma opção válida [M/F].\033[m')
while True:
    estado_civil = str(input('Estado Civil: [S/C/V/D] ')).upper().strip()[0]
    if estado_civil in 'SCVD':
        break
    print('\033[31mERRO! Informe uma opção válida [M/F].\033[m')
