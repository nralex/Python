#####################################################################################
# Faça um programa que leia 5 números e informe a soma e a média dos números.       #
#####################################################################################
números = list()
for c in range(1, 6):
    números.append(int(input(f'Digite o {c}° número: ')))
print(f'A soma dos númereos informados é {sum(números)} e a média é {sum(números) / len(números)}.')