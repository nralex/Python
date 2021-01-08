#####################################################################################################################
# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será         #
# mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá  #
# uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada #
# na tela, informando se o usuário ganhou ou perdeu o jogo.                                                         #
#####################################################################################################################
from random import randint
from random import sample
arquivo = open('6-ExerciciosComStrings\\Palavras.txt', 'r')    # Abre o arquivo 
palavras = arquivo.readlines() # Lê o arquivo
palavra = palavras[randint(0, len(palavras) - 1)].replace('\n', '').upper() # Guarda uma palavra de forma randômica em caixa alta e  sem quebra de linha.
arquivo.close() # Fecha o arquivo
embaralha = sample(palavra, len(palavra)) # Transforma a palavra sorteada em uma lista com os caracteres embaralhados
palavra_embaralhada = ''.join(embaralha) # Une os caracteres da lista em uma única string.
tentativas = 6
print(f'Embaralhei as letras de uma palavra.\nque palavra é essa?\nVocê tem {tentativas} de acertar.')
while True:
    jogada = str(input(f'{palavra_embaralhada} = ')).upper().strip() # Recebe a opção de resposta
    if jogada == palavra: # Verifica se a jogada e a palavra são iguais, caso sejam, você vence e o jogo acaba.
        print('Parabens! Você acertou!')
        break
    if tentativas == 1: # Verifica se ainda há possíbilidades de continuar o jogo, caso não haja encerra o jogo,
        print(f'GAME OVER!\nApalavra era{palavra}') # Estou encerrando em um porque  só estou retirando 1 das tentativas no próximo laço.
        break
    else: # Retira 1 de cada tentativa errada.
        tentativas -= 1
        print(f'Você ainda têm {tentativas} tentativa(s).')

