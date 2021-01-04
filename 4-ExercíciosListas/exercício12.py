#########################################################################################
# Foram anotadas as idades e alturas de 30 alunos.                                      #
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura      #
# inferior à média de altura desses alunos.                                             #
#########################################################################################
quantos = 30    # informa a quantidade de alunos
idade_referêncial = 13 # informa a idade de corte, no caso desconsideramos o que estive abaixo
turma = []
for c in range(1, quantos + 1): # Insere idade e altura
    aluno = []
    aluno.append(int(input(f'Idade do {c}° aluno: ')))
    aluno.append(float(input(f'Altura do {c}° aluno: [cm] ')))
    print('-' * 42)
    turma.append(aluno)
soma = 0
for d in range(0, len(turma)):  # Calcula a média das alturas
    soma += turma[d][1]
média = soma / len(turma)
abaixo = 0
for e in range(0, len(turma)):  # Conta os alunos com idade maior que o solicitado que possuem altura abaixo da média.
    if turma[e][0] >= idade_referêncial:
        if turma[e][1] < média:
            abaixo +=1
print(abaixo)