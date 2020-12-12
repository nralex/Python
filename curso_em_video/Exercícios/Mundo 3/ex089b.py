from time import sleep
lista = []
while True:
    nome = str(input('Nome: ')).title().strip()
    nota1 = float(input(f'Nota 1: '))
    nota2 = float(input(f'Nota 2: '))
    média = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], média])
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
    print(f'{lista[l][2]:>5.1f}')
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