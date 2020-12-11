"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
lista = [[], []]
for p in range(1, 8):
    n = int(input(f'Digite o {p}° valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    if n % 2 == 1:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print('Os valores pares digitados foram: ', lista[0])
print('Os valores impares digitados foram: ', lista[1])