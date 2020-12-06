# Crie um programa que tenha uma tupla totalmente preencida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 a 20) e mostrá-lo por extenso.
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
while True:
    if n < 0 or n > 20:
        n = int(input('Tente Novamente! Digite um número entre 0 e 20: '))
    else:
        break
print('-' *30)
print(f'Você digitou o número {extenso[n]}')
print('-' *30)