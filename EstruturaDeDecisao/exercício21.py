# Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#       Exemplo 1:  Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, 
#                   uma nota de 50, uma nota de 5 e uma nota de 1;
#       Exemplo 2:  Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
#                   uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
solicitação = int(input('Informe o valor do saque: R$'))
saque = solicitação
n100 = n50 = n10 = n5 = n1 = 0
while True:
    if 600 < saque < 10: # Para o programa se os valores informados forem menores que 10 ou maiores que 600.
        print('\033[31mNão é possível sacar o valor informado!\033[m')
        break
    else: # Separa a quantidade de notas de cada valor.
        if saque / 100 > 0 and saque >= 100:
            n100 += 1
            saque -= 100
        elif saque / 50 > 0 and saque >= 50:
            n50 += 1
            saque -= 50
        elif saque / 10 > 0 and saque >= 10:
            n10 += 1
            saque -= 10
        elif saque / 5 > 0 and saque >= 5:
            n5 += 1
            saque -= 5
        elif saque / 1 > 0 and saque >= 1:
            n1 += 1
            saque -= 1
        else:
            print(f'{n100} nota(s) de R$100,00')
            print(f'{n50} nota(s) de R$50,00')
            print(f'{n10} nota(s) de R$10,00')
            print(f'{n5} nota(s) de R$5,00')
            print(f'{n1} nota(s) de R$1,00')
            break
