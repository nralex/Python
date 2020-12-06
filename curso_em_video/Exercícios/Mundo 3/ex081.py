'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
l = []
c = 0
while True:
    c += 1
    n = int(input('Digite um valor: '))
    l.append(n)
    o = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if o not in 'SN':
        o = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if o == 'N':
        break
l.sort(reverse=True)
print(f'Você digitou {c} elementos.')    
print(f'Os valores em ordem decrescentes são {l}')
if 5 in l:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')