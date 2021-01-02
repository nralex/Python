#####################################################################################
# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...       #
# Faça um programa que gere a série até que o valor seja maior que 500.             #
#####################################################################################
n1 = 1
n2 = 1
print(n1, end=' ')
while True: 
    print(f'{n2} ', end='')
    n3 = n1 + n2
    n1 = n2
    n2 = n3 
    if n2 >= 500:
        break