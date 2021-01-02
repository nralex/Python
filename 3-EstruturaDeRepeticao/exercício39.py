#############################################################################################
# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o       #
# número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno   #
# mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais     #
# baixo, junto com suas alturas.                                                            #
#############################################################################################
altura_alunos = dict()
for c in range(1, 11):
    aluno = int(input(f'N° do {c}° aluno: '))
    altura = int(input('Altura: '))
    altura_alunos[altura] = aluno
print(f'Aluno mais alto n°:{altura_alunos[max(altura_alunos)]}, Altura {max(altura_alunos)}cm')
print(f'Aluno mais baixo n°:{altura_alunos[min(altura_alunos)]}, Altura {min(altura_alunos)}cm')