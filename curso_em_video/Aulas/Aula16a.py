lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
# Tuplas são imutáveis
print(lanche)
print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])
print(lanche[1:3])
print(lanche[-3:])
print(lanche[::-1])
print(sorted(lanche))
print(lanche)
# 1º exemplo com for
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!\n')

# 2º exemplo com for (a mesma coisa), mas pode mostrar a posição.
for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]}, na posição {c}')
print('Comi pra caramba!\n')

# 1º exemplo com for, mostrando as posições
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {pos}')
print('Comi pra caramba!\n')