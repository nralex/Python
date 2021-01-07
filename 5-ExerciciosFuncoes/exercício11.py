#####################################################################################################################
# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no   #
# formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.        #
#####################################################################################################################
def dma(d,m,a):
    meses = [ 'janeiro', 'fevereiro', 'março', 'abril', 
            'maio', 'junho', 'julho', 'agosto', 
            'setembro', 'outubro', 'novembro', 'dezembro']
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        if m == 2:
            if 1 <= d <= 29:
                print(f'{d} de {meses[m-1]} de {a}')
            else:
                return None 
    else:
        if m in (1,3, 5, 7, 8, 10, 12):
            if 1 <= d <= 31:
                print(f'{d} de {meses[m-1]} de {a}')
            else:
                return None
        if m in (4, 6, 9, 11):
            if 1 <= d <= 30:
                print(f'{d} de {meses[m-1]} de {a}')
            else:
                return None
        if m == 2:
            if 1 <= d <= 28:
                print(f'{d} de {meses[m-1]} de {a}')
            else:
                return None
    

dia = int(input('Digite o dia: '))
mês = int(input('Digite o mês: '))
ano = int(input('digite o ano: '))
dma(dia, mês, ano)