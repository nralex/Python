''' Faça um programa que calcule a soma entre todos os numeros impares 
que são múltiplos de três e que se encontram no intervalo de 1 até 500'''
s = 0
contador = 0
contador2 = 0
for c in range(1,501,2): # O número 2 no final faz pular dois n°'s
    if c % 3 == 0:
        contador += 1 # Extra 
        s += c
    contador2 += 1 # Extra 
print(f'Temos {contador2} números impares, e a soma de todos os {contador} que são divisíveis por 3 entre 1 e 500 é {s} ')