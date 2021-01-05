#####################################################################################################################
# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor    #
# jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas   #
# telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a #
# linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23,            #
# correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi          #
# encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso,  #
# e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:                               #
#       O total de votos computados;                                                                                #
#       Os números e respectivos votos de todos os jogadores que receberam votos;                                   #
#       O percentual de votos de cada um destes jogadores;                                                          #
#       O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o        #
#       percentual de votos dados a ele.                                                                            #
# Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado   #
# pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual   #
# de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o  #
# total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo.  #
# O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a  #
# cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em  #
# um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.                                     #
#####################################################################################################################
votos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    voto = int(input('N° do jogador: [0 para sair] '))
    if 1 <= voto <= 23:
        votos[voto - 1] += 1 
    elif voto == 0:
        break
    else:
        print('\033[31mInforme uma opção válida!\033[m')    
print('\nResultado da votação\n')
print(f'Foram computados {len(votos)} votos.\n')
print(f'{"Jogador":^10} {"Votos":^8} {"%":^8}')
for c in range(0, len(votos)):
    if votos[c] != 0:
        print(f'{c + 1:^10} {votos[c]:^8} {(votos[c] / len(votos)) * 100:^8.1f}% ')
mais_votado = max(votos)
melhor_jogador =  votos.index(mais_votado) + 1
print(f'O melhor jogador foi o número {melhor_jogador}, com {max(votos)} votos, correspondendo a {(max(votos) / len(votos)) * 100:^8.1f}% do total de votos.')
