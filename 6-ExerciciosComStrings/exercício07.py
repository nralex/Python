#####################################################################################################################
# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:#
#   a)  quantos espaços em branco existem na frase.                                                                 #
#   b)  quantas vezes aparecem as vogais a, e, i, o, u.                                                             #
#####################################################################################################################
n = str(input('Digite uma frase: '))
nome = n.upper()
print(f'{n.title()} possui {nome.count(" ")} espaços em branco, {nome.count("A")} letras A, {nome.count("E")} letras E, {nome.count("I")} letras I, {nome.count("O")} letras O, {nome.count("U")} letras U,')
