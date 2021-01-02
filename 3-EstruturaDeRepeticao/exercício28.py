#############################################################################################
# Faça um programa que calcule o valor total investido por um colecionador em sua coleção   #
# de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade     #
# de CDs e o valor para em cada um.                                                         #
#############################################################################################
n_de_cds = int(input('Informe a quantidade de CDs: '))
total = 0
for cada_cd in range(1, n_de_cds + 1):
        valor_cds = float(input(f'Informe o valor gasto na compra do {cada_cd}° CD: '))
        total += valor_cds
print(f"""Valor total do investimento R${total:.2f}
Valor médio gasto em cada CD R${total / cada_cd:.2f}
""")