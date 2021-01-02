#############################################################################################
# Numa eleição existem três candidatos.                                                     #
# Faça um programa que peça o número total de eleitores.                                    #
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.      #
#############################################################################################
candidatos = {'MARCOLA': 0, 'DEUSINETE': 0, 'ISOCLEITON': 0}
n = 1
for c in range(1, int(input('Quantos eleitores irão votar? ')) + 1):
    while True:
        try:
            escolha_um_candidato = int(input(f"""Eleitor {n} Informe o número do seu candidato:
        [1] - MARCOLA
        [2] - DEUSINETE
        [3] - ISOCLEITON
        Sua escolha: """))
        except:
            print('\033[31mERRO! Informe um candidáto válido!\033[m')
        else:            
            if 1 <= escolha_um_candidato <=3:
                print('\033[30mVoto válidado! Obrigado!\033[m')
                break
            else:
                print('\033[31mERRO! Informe um candidáto válido!\033[m')
    n += 1
    print('-' * 42)
    if escolha_um_candidato == 1:
        candidatos['MARCOLA'] += 1
    if escolha_um_candidato == 2:
        candidatos['DEUSINETE'] += 1
    if escolha_um_candidato == 3:
        candidatos['ISOCLEITON'] += 1
print(f'{"RESULTADO DA ELEIÇÃO":^42}')
print('-' * 42)
for i, k in enumerate(candidatos):
    print(f'{k:.<31}: {candidatos[k]:3} votos')
print('-' * 42)
