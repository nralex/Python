#############################################################################################
# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.           #
# No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.  #
# O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um         #
# programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e  #
# depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor  #
# e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos.#
# Os saltos são informados na ordem da execução, portanto não são ordenados. O programa     #
# deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve    #
# ser conforme o exemplo abaixo:                                                            #
#       Atleta: Rodrigo Curvêllo                                                            #
#                                                                                           #
#       Primeiro Salto: 6.5 m                                                               #
#       Segundo Salto: 6.1 m                                                                #
#       Terceiro Salto: 6.2 m                                                               #
#       Quarto Salto: 5.4 m                                                                 #
#       Quinto Salto: 5.3 m                                                                 #
#                                                                                           #
#       Melhor salto:  6.5 m                                                                #
#       Pior salto: 5.3 m                                                                   #
#       Média dos demais saltos: 5.9 m                                                      #
#                                                                                           #
#       Resultado final:                                                                    #
#       Rodrigo Curvêllo: 5.9 m                                                             #
#############################################################################################
competição = {}
while True:
    nome = str(input('Atleta: [0 para sair] ')).title()
    if nome == '0':
        break
    notas = []
    for c in range(1, 6):
        notas.append(float(input(f'{c}° Salto: [m] ')))
    print(f'Melhor salto: {max(notas)} m\nPior salto: {min(notas)} m')
    notas.remove(min(notas))
    notas.remove(max(notas))
    média = sum(notas) / len(notas)
    print(f'Média dos demais saltos: {média:.1f} m\n\nResultado final:\n{nome}:  {média:.1f} m\n', '-' * 42)
    competição[nome] = média
print('-' * 42)
print(f'{"RESULTADOS":^42}')
print('-' * 42)
for i, (k, v) in enumerate(competição.items()):
    print(f'{i+1}° Atleta a saltar {k}; média {v:.1f}')
print('-' * 42)
