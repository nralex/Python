#############################################################################################
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.   #
# As perguntas são:                                                                         #
#       "Telefonou para a vítima?"                                                          #
#       "Esteve no local do crime?"                                                         #
#       "Mora perto da vítima?"                                                             #
#       "Devia para a vítima?"                                                              #
#       "Já trabalhou com a vítima?"                                                        #
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.#
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como           #
# "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será    #
# classificado como "Inocente".                                                             #
#############################################################################################
respostas = [str(input("Telefonou para a vítima? ")).upper().strip()[0],
            str(input("Esteve no local do crime? ")).upper().strip()[0],
            str(input("Mora perto da vítima? ")).upper().strip()[0],
            str(input("Devia para a vítima? ")).upper().strip()[0],
            str(input("Já trabalhou com a vítima? ")).upper().strip()[0]]
print(f'{" Classificado como ":-^42}')
if respostas.count('S') == 2:
    print('Suspeita')
elif 3 <= respostas.count('S') <=4 :
    print('Cúmplice')
elif respostas.count('S') == 5:
    print('Assassino')
else:
    print('Inocente')
