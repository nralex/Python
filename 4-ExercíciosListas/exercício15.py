##########################################################################################
# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, #
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve   #
# ser armazenado). Após esta entrada de dados, faça:                                     #
#   * Mostre a quantidade de valores que foram lidos;                                    #
#   * Exiba todos os valores na ordem em que foram informados, um ao lado do outro;      #
#   * Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;#
#   * Calcule e mostre a soma dos valores;                                               #
#   * Calcule e mostre a média dos valores;                                              #
#   * Calcule e mostre a quantidade de valores acima da média calculada;                 #  
#   * Calcule e mostre a quantidade de valores abaixo de sete;                           #
#   * Encerre o programa com uma mensagem;                                               #
##########################################################################################
n = []
contador = 1
corte = 7 # a nota de corte (o 7 do enunciado)
while True:
    número = float(input(f'{contador}ª nota: [-1 para sair] '))
    if int(número) == -1:
        break
    n.append(número)
    contador += 1
média = sum(n) / len(n) # Calcule e mostre a média dos valores;
# Mostre a quantidade de valores que foram lidos;
print(f'Foram informados {len(n)} valores') # Poderia ter informado contador, mas só o coloquei a inserção ficar mais bonitinha.
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print('Os valores informados foram:') # Vou imprimir de duas maneiras:                    
print(n) # Como lista,
print('Assim é mais bonitinho:')
abaixo = acima_da_média = 0
for i, v in enumerate(n):   # Com uma formatação mai bonitinha.
    print(v, end=', ')
    if v > média:
        acima_da_média +=1  # Calcule e mostre a quantidade de valores acima da média calculada;
    if v < corte:
        abaixo += 1    # Calcule e mostre a quantidade de valores abaixo de sete;
print('\nNa ordem inversa à que foram informados, um abaixo do outro:')
for c in range(len(n) - 1, -1, -1): # Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    print(n[c])
print(sum(n)) # Calcule e mostre a soma dos valores;
print(f'Média dos valores informados: {média:.2f}')
print(f'n° de valores acima da média: {acima_da_média}')
print(f"N° de valores abaixo de {corte}: {abaixo}")
print('Volte Sempre!')# Encerre o programa com uma mensagem;