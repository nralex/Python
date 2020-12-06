n = s = c = 0
while True:
    n = int(input('Digite um número: [999 para sair] '))
    if n == 999:
        break # Encerra a repetição 
    s += n
    c += 1
print(f'Você chamou {c} números, soma vale {s}, e a média é {s / c:.2f}')