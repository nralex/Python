frase = str(input('Digite uma frase: ')).strip().upper()
f = frase.count('A')
f1 = frase.find('A') + 1
f2 = frase.rfind('A') + 1
print(f'A letra A aparece {f} na frase')
print(f'A primeira letra A apareceu na posição {f1} ')
print(f'A últuma letra A apareceu na posição {f2} ')