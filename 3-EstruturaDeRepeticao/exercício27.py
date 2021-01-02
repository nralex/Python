#############################################################################################
# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a        #
# quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter    #
# mais de 40 alunos.                                                                        #
#############################################################################################
n_de_turmas = int(input('Informe o número de turmas: '))
total_de_alunos = 0
for cada_turma in range(1, n_de_turmas + 1):
    while True:
        n_de_alunos = int(input(f'Informe o número de alunos na {cada_turma}ª turma: '))
        if n_de_alunos > 40:
            print('\033[31mERRO! As turmas não podem ter mais que 40 alunos.\033[m')
        else:
            total_de_alunos += n_de_alunos
            break
print(f'O número médio de alunos por turma é {total_de_alunos / cada_turma}')
