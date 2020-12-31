# Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')
while True:
    número = str(input('Informe um número de 1 a 7: '))
    if número not in '1234567':
        print('\033[31mValor inválido! Tente novamente\033[m')
    else:
        n = int(número)
        break
print(f'{semana[n - 1]} é o dia de número {n} da semana.')
