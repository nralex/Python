"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
"""
from time import sleep
lista = []
aluno = []
notas = []
c = 0
while True:
    nome = str(input('Nome: ')).title().strip()
    for n in range(1, 3):
        nota = float(input(f'Nota {n}: '))
        notas.append(nota)
    aluno.append(nome)
    aluno.append(notas[:])
    lista.append(aluno[:])
    aluno.clear()
    notas.clear()
    c += 1
    opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opção == 'N':
        break
print('-' * 50)
print(f'{"N°":3}', f'{"NOME":40}', f'{"MÉDIA":5}')
print('-' * 50)
listarNome = 0
for l in range(0,len(lista)):
    print(f'{f"{l}":4}', end='')
    print(f'{lista[l][0]:40}', end='')
    média = (lista[l][1][0] + lista[l][1][1]) / 2
    print(f'{média:>5.1f}')
print('-' * 50)
while True:
    qualAluno = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    if qualAluno == 999:
        print('FINALIZANDO...')
        break
    print(f'As notas de {lista[qualAluno][0]} são {lista[qualAluno][1]}')
    print('-' * 50)
sleep(1)
print(f'{"<<< VOLTE SEMPRE >>>":^50}')
