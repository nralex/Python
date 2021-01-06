#####################################################################################################################
# Faça um programa que carregue uma lista com os modelos de cinco carros                                            #
# (exemplo de modelos: FUSCA, GOL, VECTRA etc).                                                                     #
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com   #
# um litro de combustível. Calcule e mostre:                                                                        #
#   *   O modelo do carro mais econômico;                                                                           #
#   *   Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000   #
# quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de #
# exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem #
# mudar a cada execução do programa.                                                                                #
#####################################################################################################################
print('Comparativo de Consumo de Combustível\n')
carros = []
consumo = []
for c in range(1, 6):
    print(f'Veículo {c}')
    carros.append(str(input('Nome: ')))
    consumo.append(float(input('Km por litro: ')))
print('\nRelatório Final')
for i, v in enumerate(carros):
    print(f'{i+1:2} - {v:15} - {consumo[i]:6} - {1000 / consumo[i]:6.1f} litros - R$ {(1000 / consumo[i]) * 2.25:5.2f} ')
print(f'O menor consumo é do {carros[consumo.index(max(consumo))]}')
