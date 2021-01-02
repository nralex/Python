#############################################################################################
# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera          #
# verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60;        #
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.           #
#############################################################################################
idades = []
while True:
    idade = int(input('Informe a idade das pessoas aqui [999 para sair] '))
    if idade == 999:
        break
    idades.append(idade)
if 0 <= (sum(idades) / len(idades)) <= 25:
    print('A turma é JOVEM')
if 26 <= (sum(idades) / len(idades)) <= 60:
    print('A turma é ADULTA')
if (sum(idades) / len(idades)) > 60:
    print('A turma é IDOSA')
