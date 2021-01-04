#########################################################################################
# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor  #
# a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.     #
#########################################################################################
turma =[]
alunos = 10 # Informa o número de alunos
notas = 4   # Informa a quantidade de notas deve ser inserida para gerar a média
média = 7   # Informa a média de corte
for aluno in range(1, alunos + 1): # Repete para cada aluno:
    n = 0
    for nota in range(1, notas + 1):
        n += float(input(f'Informe a {nota}ª nota do {aluno}°: ')) #Insere as n notas de cada aluno.
    turma.append(n / notas) # Adiciona a média das n notas de cada aluno em uma lista (turma)
    print('-' * 42)
maior7 = 0
for i, v in enumerate(turma): # Verifica os valores da lista um a um
    if v >= média:
        maior7 +=1  # Armazena o número de alunos que alcançou a média.
print(f'Tivemos {maior7} alunos com média maior que {média}')

    
