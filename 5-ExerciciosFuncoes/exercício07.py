#####################################################################################################################
# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma      #
# conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes    #
# valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a   #
# chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a     #
# pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.   #
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor    #
# total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem    #
# atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de      #
# atraso.                                                                                                           #
#####################################################################################################################
def valorPagamento(p, d):
    if d == 0:
        return p
    else:
        return (p * 1.03 + (p * d * (0.1/100)))

prestações = []
while True:
    prestação = float(input('Valor da prestação: [0 para sair] R$ '))
    if prestação == 0:
        print(f'Foram pagas {len(prestações)}  que correspondem a um montante de R$ {sum(prestações):.2f}')
        break
    atraso = int(input('Dias em atraso: '))
    prestações.append(valorPagamento(prestação, atraso))
    print(f'O Valor atualizado da prestação é R$ {valorPagamento(prestação, atraso):.2f}')