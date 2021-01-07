#####################################################################################################################
# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com #
# o nome do mês por extenso.                                                                                        #
#                                                                                                                   #
#       Data de Nascimento: 29/10/1973                                                                              #
#       Você nasceu em  29 de Outubro de 1973.                                                                      #
#####################################################################################################################
def dma(d,m,a):
    meses = [ 'janeiro', 'fevereiro', 'março', 'abril', 
            'maio', 'junho', 'julho', 'agosto', 
            'setembro', 'outubro', 'novembro', 'dezembro']
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        if m == 2:
            if 1 <= d <= 29:
                return(f'{d} de {meses[m-1]} de {a}')
            else:
                return None 
    else:
        if m in (1,3, 5, 7, 8, 10, 12):
            if 1 <= d <= 31:
                return(f'{d} de {meses[m-1]} de {a}')
            else:
                return None
        if m in (4, 6, 9, 11):
            if 1 <= d <= 30:
                return(f'{d} de {meses[m-1]} de {a}')
            else:
                return None
        if m == 2:
            if 1 <= d <= 28:
                return(f'{d} de {meses[m-1]} de {a}')
            else:
                return None
    

s = str(input('Data de Nascimento: xx/xx/xxxx '))
dn = s.split("/", 2)
print(f'Você nasceu em {dma(int(dn[0]), int(dn[1]), int(dn[2]))}.')