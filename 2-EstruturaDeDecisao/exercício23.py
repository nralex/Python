# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
número = str(input('Digite um número: ')).replace(',', '.')
n = float(número)
if n == int(n): # Preferi usar o int, que ignora os calores das casas decimais.
    print(f'{n} é um número inteiro')
else:
    print(f'{n} é um número decimal (flutuante)')