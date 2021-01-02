#############################################################################################
# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:            #
#   a)  Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;        #
#   b)  Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;                          #
#   c)  A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do #
#       percentual do ano anterior.                                                         #
# Faça um programa que determine o salário atual desse funcionário.                         #
# Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial   #
# do funcionário.                                                                           #
#############################################################################################
from datetime import date
salário_inicial = 1000
taxa_aumento = 0.015
for c in range(1996, date.today().year):
    salário_atual = salário_inicial * (1 + taxa_aumento)
    print(f'Ano {c}; Percentual {taxa_aumento * 100}%; Salário R$ {salário_atual:.2f}')
    taxa_aumento *= 2    
    salário_inicial = salário_atual
print('-' * 42)
print(f'Salário atual: R$ {salário_atual:.2f} ')
