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

from random import randint
arquivo = open('6-ExerciciosComStrings\\Palavras.txt', 'r')    # Abre o arquivo 
palavras = arquivo.readlines() # Lê o arquivo
palavra = palavras[randint(0, len(palavras) - 1)].replace('\n', '').upper() # Guarda uma palavra de forma randômica em caixa alta e  sem quebra de linha.
arquivo.close()
# Guarda cada letre da palavra escolhida em uma lista e cria uma lista com os paços com o mesmo tamanho da palavra  escolhida.
p = []
acertos = []
for c in range(0, len(palavra)):
    p.append(palavra[c])
    acertos.append(' __')
tentativas = 6
print(f'Vamos iniciar o jogo da forca.\nVocê tem {tentativas} tentativas')

while True:   
    letra = input('Digite uma letra: ').upper().strip()[0] # Recebe cada letra sempre em maiúsculo.
    if letra not in p: # verifica se a letra se encontra na lista de referência e
        tentativas -= 1 # retira uma tentativa a cada tentativa errada
        print(f'\033[31mVocê errou! Restam {tentativas} tentativa(s)\033[m')
    if tentativas == 0: # si do jogo quando as tentativas chegam a zero e apresenta a palavra
        print('GAME OVER!')
        print(f'A palavra era: {palavra}')
        break
    for i, l in enumerate(p): # A cada tentativa confere se a letra apresentada se encontra na lista de referência
        if l == letra: # Substitui e mostra caso tenha acertado a letra.
            acertos[i] = l
            print(l, end='')
        else: # Caso tenha errado mostra os espaços em branco e as letras que ja acertou na ordem correta da palavra.
            print(acertos[i], end='')    
    print()
    if p == acertos: # Quando  a lista de referência e a lista de acerto s se iguala, acaba o jogo e você ganha.
        print('Acertou! Fim de Jogo!')
        break