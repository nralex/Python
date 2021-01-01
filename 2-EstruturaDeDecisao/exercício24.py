# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#   a)  par ou ímpar;
#   b)  positivo ou negativo;
#   c)  inteiro ou decimal.
n1 = float(input('Informe um número: '))
n2 = float(input('Informe mais um número: '))
while True:
    operação = int(input("""Qual operação deseja realizar:
    [1] adição
    [2] subtração
    [3] multiplicação
    [4] divisão 
    Informe sua escolha: """))
    if 1 <= operação <= 4:
       break
    else:
         print('\033[31mERRO! Escolha uma opção válida.\033[m')
# Resolve as operações como solicitado.
if operação == 1:
    resultado = n1 + n2
    print(f'{n1} + {n2} = {resultado}')
if operação == 2:
    resultado = n1 - n2
    print(f'{n1} - {n2} = {resultado}')
if operação == 3:
    resultado = n1 * n2
    print(f'{n1} x {n2} = {resultado}')
if operação == 4:
    resultado = n1 / n2
    print(f'{n1} ÷ {n2} = {resultado}')
# inclui as demais informações.
if resultado == int(resultado): # Como não há classificação de par ou impar para números fracionários já resolvemos isso agora.
    if resultado % 2 == 0:
        print(f'{resultado} é par.')
    else:
        print(f'{resultado} é impar.')
    if resultado > 0:
        print(f'{resultado} é positivo.')
    else:
        print(f'{resultado} é negativo.')
if resultado == 0: # Zero é um número inteiro, mas não podemos classificar como positivo ou negativo.
    print(f'{resultado} é um número inteiro')
if resultado != int(resultado): # Números fracionários 
    if resultado > 0:
        print(f'{resultado} é positivo.')
    else:
        print(f'{resultado} é negativo.')
    print(f'{resultado} é decimal.')
else:
    print(f'{resultado} é inteiro.')