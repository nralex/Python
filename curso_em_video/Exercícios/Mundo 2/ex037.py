número = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'O numero {número} convertido para BINÁRIO é igual a {bin(número)[2:]}')
elif opção == 2:
    print(f'O numero {número} convertido para OCTAL é igual a {oct(número)[2:]}')
elif opção == 3:
    print(f'O numero {número} convertido para HEXADECIMAL é igual a {hex(número)[2:]}')
else:
    print(f'{opção} não é uma opção válida. Tente novamente!')

