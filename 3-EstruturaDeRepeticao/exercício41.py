##############################################################################################
# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes     #
# dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.        #
#   Os juros e a quantidade de parcelas seguem a tabela abaixo:                              #
#       Quantidade de Parcelas      % de Juros sobre o valor inicial da dívida               #
#       1                           0                                                        #
#       3                           10                                                       #
#       6                           15                                                       #
#       9                           20                                                       #
#       12                          25                                                       #
#   Exemplo de saída do programa:                                                            #
#       Valor da Dívida     Valor dos Juros     Quantidade de Parcelas      Valor da Parcela #
#       R$ 1.000,00         0                   1                           R$  1.000,00     #
#       R$ 1.100,00         100                 3                           R$    366,00     #
#       R$ 1.150,00         150                 6                           R$    191,67     #
##############################################################################################
parcelas = (1, 3, 6, 9, 12)
print('-' * 101)
print(f'{"CALCULO DE PARCELAS E MONTANTE":^101}')
print('-' * 101)
dívida = float(input('Informe o valor da compra: R$ '))
print('-' * 101)
print(f'|{"Valor da Dívida":^24}|{"Valor dos Juros":^24}|{"Quantidade de Parcelas":^24}|{"Valor da Parcela":^24}|')
print('-' * 101)
for c in range(1, 6):
    quantidade_parcelas = parcelas[c-1]
    if  quantidade_parcelas == 1:
        taxa = 1
    if  quantidade_parcelas == 3:
        taxa = 1.1
    if  quantidade_parcelas == 6:
        taxa = 1.15
    if  quantidade_parcelas == 9:
        taxa = 1.2
    if  quantidade_parcelas == 12:
        taxa = 1.25
    print(f'|{f"R$ {dívida * taxa:.2f}":^24}|{f"R$ {dívida * (taxa - 1):.2f}":^24}|{parcelas[c-1]:^24}|{f"R$ {(dívida * taxa) / parcelas[c-1]:.2f}":^24}|')
print('-' * 101)