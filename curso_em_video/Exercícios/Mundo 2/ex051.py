'''Desenvolva um programa que leia o primeiro termo e a 
razão de uma PA. No final. mostre os 10 primeiros termos
dessa progressão.'''
a = int(input('Primeiro de termos: '))
r = int(input('Razão: '))
q = int(input('Quantos termos: ')) # Inclui para perguntar o número de termos
# Deu certo mas a outra forma é melhor!
'''for c in range(1,11):
    print(f'a{c} = {a + (c - 1) * r}', end='; ')'''
for c in range(a, a + q * r, r):
     print(c, end=' - ')
print('ACABOU')