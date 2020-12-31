# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina 
# ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, 
# o conceito correspondente e a mensagem “APROVADO” se 
# o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
notas = []
for c in range(1, 3):
    nota = str(input(f'Digite a {c}ª nota:[x,x] ')).replace(',', '.')
    notas.append(float(nota))
media = sum(notas) / len(notas)
if 10 >= media > 9:
    conceito = 'A'
elif 9 >= media > 7.5:
    conceito = 'B'
elif 7.5 >= media > 6:
    conceito = 'C'
elif 6 >= media > 4:
    conceito = 'D'
elif 4 >= media > 0:
    conceito = 'E'
else:
    print('\033[31mValor inválido! ERRO de digitação!\033[m')
if conceito in 'ABC':
    menságem = 'APROVADO'
elif conceito in 'DE':
    menságem = 'REPROVADO'
print(f"""
As notas apresentadas foram {notas}
A média das notas apresentadas é {media}
O conceito para a média apresentada é {conceito}
Com o conceito apresentado o aluno se encontra {menságem}
""")