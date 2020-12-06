'''Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e 
qual foi o maior e o menor valores lidos. O programa deve 
perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
c = soma = maior = menor = 0
opção = 'S'
while opção == 'S':
    n = int(input('Digite um número: '))
    c += 1
    soma += n  
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        else:
            menor = n
    opção = str(input('Quer continuar? [S/N] ')).upper().strip()
print(f'Você digitou {c} números e a média foi {soma / c}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
