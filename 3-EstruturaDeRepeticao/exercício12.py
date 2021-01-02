#####################################################################################
# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número     #
# inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a     #
# tabuada. A saída deve ser conforme o exemplo abaixo:                              #
# Tabuada de 5:                                                                     #
# 5 X 1 = 5                                                                         #
# 5 X 2 = 10                                                                        #
# ...                                                                               #
# 5 X 10 = 50                                                                       #
#####################################################################################
tabuada = int(input('Mostre a tabuada de: '))
print(f'{f"Tabuada de {tabuada}":^13} ')
print('~' * 13)
for c in range(1, 11):
    print(f'{tabuada} x {c:<2} = {tabuada * c} ')
print('~' * 13)