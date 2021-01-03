#############################################################################################
# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes #
# de trânsito. Foram obtidos os seguintes dados:                                            #
#   a)  Código da cidade;                                                                   #
#   b)  Número de veículos de passeio (em 1999);                                            #
#   c)  Número de acidentes de trânsito com vítimas (em 1999).                              #
# Deseja-se saber:                                                                          #
#   d)  Qual o maior e menor índice de acidentes de transito e a que cidade pertence;       #
#   e)  Qual a média de veículos nas cinco cidades juntas;                                  #
#############################################################################################
from datetime import date
maior = código_maior = menor = código_menor = carros = acidentes_2000 = média_acidentes = 0
nc_2000 = 1
for c in range(1, 6):
    print('-' * 60)
    # Solicita Código da cidade
    código = int(input(f'Código da {c}ª cidade: '))
    # Solicita Número de veículos de passeio
    veículos = int(input(f'Número de veículos de passeio (em {date.today().year - 1}): '))
    # Solicita úmero de acidentes de trânsito com vítimas
    acidentes = int(input(f'Número de acidentes de trânsito com vítimas (em {date.today().year - 1}): '))
    # Mostra o maior e menor índice de acidentes de transito e a que cidade pertence
    if acidentes > maior:
        maior = acidentes
        código_maior = código
    if código_menor == 0:
        menor = acidentes
        código_menor = código
    if acidentes < menor:
        menor = acidentes
        código_menor = código
    # Mostra a média de veículos nas cinco cidades juntas
    carros += veículos
    média_veículos = carros / c
    
print('-' * 60)
print(f"""O maior indíce de acidentes foi {maior} na cidade de código {código_maior}
O menor indíce de acidentes foi {menor} na cidade de código {código_menor}
A média de veículos nas {c} cidades foi {média_veículos}""")
