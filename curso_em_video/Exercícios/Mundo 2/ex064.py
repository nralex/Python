#Crie um programa que leia vários números inteiros pelo teclado. 
'''O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números 
foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
n = c = s = 0
n = int(input('Digite um número [999 para para]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número [999 para para]: '))
print(f'Você digitou {c} numeros e a soma entre eles é {s}.')