#####################################################################################
# Altere o programa anterior permitindo ao usuário informar as populações e as      #
# taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.     #
#####################################################################################
contador = 1
while True:
    while True: # Solicita e valida população
        a = int(input('Informe a população do país A: '))
        b = int(input('Informe a população do país B: '))
        if a < b:
            break
        print('\033[31mERRO! A população do país B não pode ser maior que do país A\033[m')
    while True: # Solicita e valida as taxas de crescimento
        taxa_a = 1 + (float(input('Informe a taxa de crescimento do país A: '))/100)
        taxa_b = 1 + (float(input('Informe a taxa de crescimento do país B: '))/100)
        if taxa_a > taxa_b:
            break
        print('\033[31mERRO! A taxa de crescimento do país B não pode ser menor que do país A\033[m')
    while True: # Faz o calculo de fato
        a *= taxa_a
        b *= taxa_b
        contador += 1
        if a >= b:
            print(f'São necessários {contador} anos para que a população do país A ultrapasse a população do país B')
            break    
    while True: # Pergunta se quer continuar
        opção = str(input('Quer repetir a operação? [S/N] ')).upper().strip()[0]
        if opção not in 'SN':
            print('\033[31mERRO! Informe uma opção válida [S/N]\033[m')
        else:
            break
    if opção == 'N': # Sai do programa
        break
