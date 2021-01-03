#################################################################################################
# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a        #
# pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve        #
# fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas         #
# pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima      #
# informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). #
# As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o    #
# exemplo abaixo:                                                                               #
#       Atleta: Aparecido Parente                                                               #
#       Nota: 9.9                                                                               #
#       Nota: 7.5                                                                               #
#       Nota: 9.5                                                                               #
#       Nota: 8.5                                                                               #
#       Nota: 9.0                                                                               #
#       Nota: 8.5                                                                               #
#       Nota: 9.7                                                                               #
#                                                                                               #
#       Resultado final:                                                                        #
#       Atleta: Aparecido Parente                                                               #
#       Melhor nota: 9.9                                                                        #
#       Pior nota: 7.5                                                                          #
#       Média: 9,04                                                                             #
#################################################################################################
nome = str(input('Atleta: ')).title()
notas = []
for c in range(1, 8):
    notas.append(float(input(f'{c}° Nota: ')))
print(f'\nResultado Final:\nAtleta: {nome}')
print(f'Melhor nota: {max(notas)}\nPior nota: {min(notas)}')
notas.remove(min(notas))
notas.remove(max(notas))
média = sum(notas) / len(notas)
print(f'Média: {média:.1f}')
    