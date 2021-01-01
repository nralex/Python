# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
#       A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#       A mensagem "Reprovado", se a média for menor do que sete;
#       A mensagem "Aprovado com Distinção", se a média for igual a dez.
notas = []
for c in range(1, 3):
    nota = str(input(f'Digite a {c}ª nota: ')).replace(',', '.')
    notas.append(float(nota))
media = sum(notas) / len(notas)
print(f'Suá média foi {media:.1f}')
if media == 10:
    print('APROVADO COM DISTINÇÃO')
elif media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')