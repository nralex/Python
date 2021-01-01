# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data_completa = str(input('Informe uma data: [dd/mm/aaaa] '))
valida = True
dma = data_completa.split('/') # converte data_completa em uma lista
data = []
for c in dma: # Conversão das strings de dma em inteiro
    data.append(int(c))
# Verifica se há mais que 12 meses no ano
if data[1] > 12:
    valida = False
# Verifica se há mais que 31 dias nos meses em que há 31 dias
elif data[1] == 1 or data[1] == 3 or data[1] == 5 or data[1] == 7 or data[1] == 8 or data[1] == 10 or data[1] == 12:
    if data[0] > 31:
        valida = False
# Verifica se há mais que 30 dias nos meses em que há 30 dias
elif data[1] == 4 or data[1] == 6 or data[1] == 9 or data[1] == 11:
    if data[0] > 30:
        valida = False
# Verifica se é uma no bissexto e sé há mais dias que deveria.
elif data[1] == 2:
    if (data[2] % 4 == 0 and data[2] % 100 != 0) or data[2] % 400 == 0:
        if data[0] > 29:
            valida = False
    else:
        if data[0] > 28:
            valida = False
if valida == False:
    print(f'{data_completa} não é uma data válida!')
else:
    print(f'{data_completa} é uma data válida!')
