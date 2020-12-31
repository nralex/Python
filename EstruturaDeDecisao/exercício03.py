# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
if sexo not in 'MF':
    print('\033[31mSexo Inválido\033[m')
else:
    if sexo == 'F':
        print(f'{sexo} - Feminino')
    if sexo == 'M':
        print(f'{sexo} - Masculino')
        