# Faça um Programa para leitura de três notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e presentar:
#   a)  A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#   b)  A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#   c)  A mensagem "Aprovado com Distinção", se a média for igual a 10.
notas = []
for c in range(1, 4):
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
