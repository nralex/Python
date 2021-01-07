#####################################################################################################################
# Palíndromo. Um palíndromo é uma sequencia de caracteres cuja leitura é idêntica se feita da direita para esquerda #
# ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são       #
# ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um    #
# programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.                         #
#####################################################################################################################
t = str(input('Digite uma frase [Favor não digitar pontuação e caracteres especiais(ç,~,^,´,`)]\n'))
if t.replace(' ', '').upper() == t[::-1].replace(' ', '').upper():
    print(f'{t} é um PALINDROMO')
else:
    print(f'{t} não é um PALINDROMO')