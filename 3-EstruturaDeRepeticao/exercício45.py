#############################################################################################
# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o    #
# programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o     #
# gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por      #
# resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro  #
# aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:             #
#   a)  Maior e Menor Acerto;                                                               #
#   b)  Total de Alunos que utilizaram o sistema;                                           #
#   c)  A Média das Notas da Turma.                                                         #
#           Gabarito da Prova:                                                              #
#           01 - A                                                                          #
#           02 - B                                                                          #
#           03 - C                                                                          #
#           04 - D                                                                          #
#           05 - E                                                                          #
#           06 - E                                                                          #
#           07 - D                                                                          #
#           08 - C                                                                          #
#           09 - B                                                                          #
#           10 - A                                                                          #
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite  #
# o gabarito da prova antes dos alunos usarem o programa.                                   #
#############################################################################################
gabarito = []
for c in range(1, 11):
    resposta = str(input(f'Informe a resposta da questão {c}: ')).upper().strip()[0]
    gabarito.append(resposta)
print(gabarito)
notas = []
while True:
    nota = 0
    for c in range(0, len(gabarito)):
        while True:
            insert = str(input(f'Resposta da {c + 1}ª questão: ')).upper().strip()[0]
            if insert in 'ABCDE ':
                break
            else:
                print('\033[31mInforme uma opção válida\033[m')                
        if insert == gabarito[c]:
            nota += 1
    print(f'Sua nota é {nota}')
    notas.append(nota)
    while True:
        saída = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if saída in 'SN':
            break
        else:
            print('\033[31mInforme uma opção válida\033[m') 
    if saída == 'N':
        break
print(f"""
Maior nota: {max(notas)}
Menor nota: {min(notas)}
Total de alunos que utilizaram o sistema: {len(notas)}
Media de notas da turma: {sum(notas) / len(notas):.2f}
""")
