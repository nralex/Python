#####################################################################################################
# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.   #
# Exemplo:                                                                                          #
#  12376489                                                                                         #
#  => 98467321                                                                                      #
#####################################################################################################
n = int(input('Digite um numero inteiro positivo:\n'))
s = str(n)
for c in range(len(s), 0, -1):
    print(s[c-1], end='')
