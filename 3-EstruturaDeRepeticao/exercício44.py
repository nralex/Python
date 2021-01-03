#############################################################################################
# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio   #
# de código. Os códigos utilizados são:                                                     #
#   1 , 2, 3, 4  - Votos para os respectivos candidatos                                     #
#   (você deve montar a tabela ex: 1 - José/ 2- João/etc)                                   #
#   5 - Voto Nulo                                                                           #
#   6 - Voto em Branco                                                                      #
# Faça um programa que calcule e mostre:                                                    #
#   *   O total de votos para cada candidato;                                               #
#   *   O total de votos nulos;                                                             #
#   *   O total de votos em branco;                                                         #
#   *   A percentagem de votos nulos sobre o total de votos;                                #
# A percentagem de votos em branco sobre o total de votos.                                  #
# Para finalizar o conjunto de votos tem-se o valor zero.                                   #
#############################################################################################
candidatos = {
    1: 'Helena',
    2: 'Alice',
    3: 'Miguel', 
    4: 'Arthur'}
v1 = v2 = v3 = v4 = vn = vb = total = 1
votos = {'Branco': 0, 'Nulo': 0}
while True:
    for indice, (chave, valor) in enumerate(candidatos.items()):
        print(f'{chave} - {valor}')
    try:
        voto = int(input('Digite o número do seu candidato: [0 para sair] '))
    except:
        voto = 5
    if voto == 1:
        votos[candidatos[1]] = v1
        v1 +=1
    if voto == 2:
        votos[candidatos[2]] = v2
        v2 +=1
    if voto == 3:
        votos[candidatos[3]] = v3
        v3 +=1
    if voto == 4:
        votos[candidatos[4]] = v4
        v4 +=1
    if voto == 5:
        votos['Branco'] = vb
        vb +=1
    if voto > 5:
        votos['Nulo'] = vn
        vn +=1
    total += 1
    print('-' *42)
    if voto == 0:
        print(f'{"QUANTITATIVO DOS VOTOS":^42}')
        print('-' *42)
        break
for i, (k, v) in enumerate(votos.items()):
    print(f'{k:7}: {v:>3} votos ')
percentual_branco = (votos['Branco'] / total) * 100
percentual_nulo = (votos['Nulo'] / total) * 100
print(f'{percentual_branco:.1f}% do total de votos foi branco')
print(f'{percentual_nulo:.1f}% do total de votos foi nulo')
print('-' *42)
