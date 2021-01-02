#####################################################################################
# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...         #
# Faça um programa capaz de gerar a série até o n−ésimo termo.                      #
#####################################################################################
n_ésimo = int(input('n-ésimo n°: '))
n1 = 1
n2 = 1
print(n1, end=' ')
for c in range (1,n_ésimo): 
    print(f'{n2} ', end='')
    n3 = n1 + n2
    n1 = n2
    n2 = n3  
