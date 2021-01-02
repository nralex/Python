#############################################################################################
# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que    #
# leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior   #
# temperaturas informadas, bem como a média das temperaturas.                               #
#############################################################################################
temperaturas = []
contador = 1
while True:
    nova_temperatura = float(input(f'{contador}ª Temperatura [999 para sair] '))
    if nova_temperatura == 999:
        print('-' * 42)
        break
    temperaturas.append(nova_temperatura)
    contador +=1 
print(f'Menor temperatura {min(temperaturas)}°C')
print(f'Maior temperatura {max(temperaturas)}°C')
print(f'Média das temperaturas {sum(temperaturas) / contador:.1f}°C')