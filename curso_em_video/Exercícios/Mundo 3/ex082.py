'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares 
e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
l = []
while True:
    l.append(int(input('Digite um número: ')))
    o = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if o not in 'SN':
        o = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if o == 'N':
        break
print(f'A lista completa é {l}')
c = 0
par = []
while c <= len(l) - 1:
    if l[c] % 2 == 0:
        par.append(l[c])
    c += 1
print(f'A lista de pares é {par}')
d = 0
impar = []
while d <= len(l) - 1:
    if l[d] % 2 != 0:
        impar.append(l[d])
    d += 1
print(f'A lista de impares é {impar}')