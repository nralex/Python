#####################################################################################################################
# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer#
# um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses  #
# que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.#
# Foi requisitado que você desenvolva um programa para registrar este levantamento.                                 #
# O programa deverá receber um número indeterminado de entradas, cada uma contendo:                                 #
# um número de identificação do mouse o tipo de defeito:                                                            #
#       necessita da esfera;                                                                                        #
#       necessita de limpeza;                                                                                       #
#       necessita troca do cabo ou conector;                                                                        #
#       quebrado ou inutilizado                                                                                     #
#       Uma identificação igual a zero encerra o programa.                                                          #
# Ao final o programa deverá emitir o seguinte relatório:                                                           #
#####################################################################################################################
identificação = []
situação = []
defeito = ['necessita da esfera', 'necessita de limpeza', 'necessita troca do cabo ou conector', 'quebrado ou inutilizado']
contador = 1
while True:
    código = int(input(f'{contador}° N° de identificação: [0 para sair] '))
    if código == 0:
        break
    elif código not in identificação:
        contador += 1 # Incluído apenas para ajudar na formatação da menságem de entrada.
        identificação.append(código)
        for i, v in enumerate(defeito):
            print(f'[{i + 1}] - {v} ')
        while True:
            estado =int(input('Informe o estado o item: '))
            if 1 <= estado <= len(defeito):
                situação.append(estado)
                break
            else:
                print('\033[31mInforme uma opção válida\033[m')
    else:
        print('\033[31mCódigo já informado!\033[m')
print()
print(f'Quantidade de mouses: {len(identificação)}\n') # poderia ter usado o comprimento de situação ou o contador.
print(f'{"Situação":40} {"Quantidade"} {"Percentual":>12}')
for i, v in enumerate(defeito):
     print(f'{i + 1}- {v:37} {situação.count(i + 1):>10}   {((situação.count(i + 1)) / len(situação)) * 100:>10}%')

