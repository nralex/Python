n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
# \n qubra a linha da impressão  e .2f limita o número de casas decimais depois do ponto em duas casas
print(f'A soma vale {n1+n2}; \no produto é {n1*n2}; \na divisão é {n1/n2:.2f}; \na divisão inteira é {n1//n2}; \no resto da divisão é {n1%n2}; \ne a potência é {n1**n2}. ')
#end='' concatena as linhas de impressão.
print(f'A soma vale {n1+n2}; o produto é {n1*n2}; a divisão é {n1/n2:.1f}; ', end='')
print(f'na divisão inteira é {n1//n2}; o resto da divisão é {n1%n2}; e a potência é {n1**n2}.')