#########################################################################################
# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação   #
# no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.    #
#########################################################################################
quantidade = 5
idade = []
altura = []
for c in range(1, quantidade +1):
    idade.insert(0, int(input(f'Idade da {c}ª pessoa: ')))
    altura.insert(0, int(input(f'Altura da {c}ª pessoa: [cm] ')))
for r in range(0, quantidade):
    print(f'Idade: {idade[r]}, Altura: {altura[r]} ')