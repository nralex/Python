#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
f = str(input('Digite uma frase: ')).replace(' ', '').upper()
#i = f[::-1] minha inversão
# inversão com for:
i = ''
for c in range(len(f) -1, -1, -1):
    i += f[c]
print(f'O inverso de {f} é {i} ')
if f == i:
    print('A frase digitada é um palindromo!')
else:
    print('A frase digitada não é um palindromo!')
