#####################################################################################################################
# Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras,#
# como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet        #
# reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir  #
# os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras.     #
# Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.                              #
#####################################################################################################################
dicionário_leet = { 'A':'@','B':'8','C':'(','D':'D','E':'3','F':'F','G':'6','H':'#','I':'1','J':'J','K':'K','L':'-7',
                    'M':'M','N':'N','O':'0','P':'P','Q':'Q','R':'Я','S':'5','T':'+','U':'U','V':'V','W':'W','X':'X',
                    'Y':'Y','Z':'%', ' ': ' '}
texto = str(input('Digite o seu texto: [Sem acento] '))
for i in texto.upper():
    if i.isalpha():
        print(dicionário_leet[i], end='')
    else:
        print(' ', end='')
    