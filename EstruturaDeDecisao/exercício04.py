# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
vogais = 'AEIOU'
letra = str(input('Digite uma letra: ')).upper().strip()[0]
if letra.isnumeric(): # Verifico se se trata de um número.
    print(f'{letra} é um número')
elif letra not in vogais:
    print(f'{letra} é uma consoante.')
else:
    print(f'{letra} é uma vogal.')
