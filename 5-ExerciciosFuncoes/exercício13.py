#####################################################################################################################
# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.              #
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual  #
# a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores     #
# dentro da faixa de forma elegante.                                                                                #
#####################################################################################################################
def moldura(l=1,c=1):
    if l<1 or l>20 or c<1 or c>20:
        l = 10
        c = 16
    print('+', '-' * l, '+')
    for i in range(0, c):
        print('|', ' ' * l, '|')
    print('+', '-' * l, '+')


moldura(40,40)