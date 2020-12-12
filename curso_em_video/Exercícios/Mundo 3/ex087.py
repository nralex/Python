""" Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.

0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
   for p in range(0, 3):
      matriz[l][p] = int(input(f'Digite um valor para [{l}] [{p}] '))
print('+=' * 15)
for l in range(0, 3):
   for p in range(0, 3):
      print(f'[{matriz[l][p]:^5}]', end='')
   print()
print('+=' * 15)
soma = 0
for l in range(0, 3):
   for p in range(0, 3):
      if matriz[l][p] % 2 == 0:
         soma += matriz[l][p]
print(f'A soma dos valores pares é {soma}')
terceiraColuna = 0
for p in range(0, 3):
   terceiraColuna += matriz[p][2]
print(f'A soma dos valores da terceira coluna é {terceiraColuna}')
segundaLinha = 0
for p in range(0, 3):
   if matriz[1][p] == 0:
      segundaLinha = matriz[1][p]
   if matriz[1][p] > segundaLinha:
      segundaLinha = matriz[1][p]
print(f'O maior valor da segunda linha é {segundaLinha}')