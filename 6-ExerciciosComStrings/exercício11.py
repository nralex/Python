#####################################################################################################################
# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e     #
# escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.                              #
#                                                                                                                   #
#       Digite uma letra: A                                                                                         #
#       -> Você errou pela 1ª vez. Tente de novo!                                                                   #
#                                                                                                                   #
#       Digite uma letra: O                                                                                         #
#       A palavra é: _ _ _ _ O                                                                                      #
#                                                                                                                   #
#       Digite uma letra: E                                                                                         #
#       A palavra é: _ E _ _ O                                                                                      #
#                                                                                                                   #
#       Digite uma letra: S                                                                                         #
#       -> Você errou pela 2ª vez. Tente de novo!                                                                   #
#####################################################################################################################
'''
from random import randint
arquivo = open('6-ExerciciosComStrings\\Palavras.txt', 'r')    # Abre o arquivo 
palavras = arquivo.readlines() # Lê o arquivo
palavra = palavras[randint(0, len(palavras) - 1)].replace('\n', '').upper() # Guarda uma palavra de forma randômica em caixa alta e  sem quebra de linha.
print(palavra)
'''
palavra = 'PATO'
letra = 'A'
vazio = '__ ' * len(palavra)

if letra in palavra:
    print(vazio)