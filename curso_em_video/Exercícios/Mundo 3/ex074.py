# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import sample
n = sample(range(10),5)
print('Os valores sorteados foram: ', end='')
c = 0
for t in n:
    print(t, end=' ')
    if c == 0:
        menor = t
        maior = t
    else:
        if t < menor:
            menor = t
        if t > maior:
            maior = t 
    c += 1
print()
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
print() # É frustante só saber disso na correção, mas ao menos pratiquei a maneira mais complexa.
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')