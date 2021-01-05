#####################################################################################################################
# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de        #
# organizações:                                                                                                     #
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado   #
# da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não      #
# deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das        #
# opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá      #
# calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.                               #
#####################################################################################################################
votos = [0, 0, 0, 0, 0, 0]
sistemas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
while True:
    print('-' * 57)
    print('Qual o melhor Sistema Operacional para uso em servidores?\n\nAs possíveis respostas são:\n')
    for c in range(1, len(sistemas)+1):
        print(f'{c} - {sistemas[c-1]}')
    voto = int(input('[0 para sair] '))
    if voto == 0:
        break
    elif 1 <= voto <= 6:
        votos[voto - 1] +=1
    else:
        print('\033[31mInforme uma opção válida!\033[m')  

print(f'{"Sistema Operaciomal":19} {"Votos":5} {"%":^5}')
print('-' * 32)
for c in range(0, len(sistemas)):
    print(f'{sistemas[c]:19} {votos[c]:^5} {(votos[c] / sum(votos)) * 100:5.1f}% ')
print('-' * 32)
print(f'{"Total":19} {sum(votos):^5}')

mais_votado = max(votos)
melhor_sistema =  votos.index(mais_votado)
print(f'O Sistema Operacional mais votado foi o {sistemas[melhor_sistema]}, com {votos[melhor_sistema]:5.1f} votos, correspondendo a {(votos[c] / sum(votos)) * 100}% dos votos.')
