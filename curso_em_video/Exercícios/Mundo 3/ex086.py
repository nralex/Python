""" Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
No final, mostre a matriz na tela, com a formatação correta. """
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
   for p in range(0, 3):
      matriz[l][p] = int(input(f'Digite um valor para [{l}] [{p}] '))
print('+=' * 15)
for l in range(0, 3):
   for p in range(0, 3):
      print(f'[{matriz[l][p]:^5}]', end='')
   print()