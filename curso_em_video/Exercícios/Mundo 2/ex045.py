# JOQUEMPÔ
print('-+' * 20)
print('Vamos brincar de pedra, papel e tesoura?')
print('+-' * 20)
print('''Escolha uma opção!
[1] Pedra
[2] Papel
[3] Tesoura
Juro que não vou olhar!
''')
j1 = int(input('Joquempô: '))
if j1 == 1:
    j1 = 'PEDRA'
elif j1 == 2:
    j1 = 'PAPEL'
elif j1 == 3:
    j1 = 'TESOURA'
elif j1 > 3:
    print('Insira uma jogada válida')
from random import choice
jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
j2 = choice(jogadas)
if j1 == j2:
    print(f'Você jogou {j1}, e eu joguei {j2}. Então EMPATAMOS')
# Pedra
elif j1 == 'PEDRA' and j2 == 'TESOURA':
    print(f'Você jogou {j1}, e eu joguei {j2}. Então VOCÊ GANHOU')
elif j1 == 'PEDRA' and j2 == 'PAPEL':
    print(f'Você jogou {j1}, e eu joguei {j2}. Então VOCÊ PERDEU')
# Papel
elif j1 == 'PAPEL' and j2 == 'PEDRA':
    print(f'Você jogou {j1}, e eu joguei {j2}. Então VOCÊ GANHOU')
elif j1 == 'PAPEL' and j2 == 'TESOURA':
    print(f'Você jogou {j1}, e eu joguei {j2}. Então VOCÊ PERDEU')
# Tesoura
elif j1 == 'TESOURA' and j2 == 'PAPEL':
    print(f'Você jogou {j1}, e eu joguei {j2}. Então VOCÊ GANHOU')
elif j1 == 'TESOURA' and j2 == 'PEDRA':
    print(f'Você jogou {j1}, e eu joguei {j2}. Então VOCÊ PERDEU')