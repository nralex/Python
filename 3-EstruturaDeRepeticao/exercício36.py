#############################################################################################
# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado #
# pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o     #
# valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:  #
#       Montar a tabuada de: 5                                                              #
#       Começar por: 4                                                                      #
#       Terminar em: 7                                                                      #
#                                                                                           #
#       Vou montar a tabuada de 5 começando em 4 e terminando em 7:                         #
#       5 X 4 = 20                                                                          #
#       5 X 5 = 25                                                                          #
#       5 X 6 = 30                                                                          #
#       5 X 7 = 35                                                                          #
#   Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.          #
#############################################################################################
tabuada = int(input('Mostre a tabuada de: '))
while True:
    início = int(input('Começar por: '))
    fim = int(input('Terminar em: '))
    if fim > início:
        break
    else:
        print('\033[31mERRO! Não é possível calcular inserindo um número final menor que o inicial.\033[m')
print(f'{f"Vou montar a tabuada de {tabuada} começando em {início} e terminando em {fim}:":^42} ')
for c in range(início, fim + 1):
    print(f'{tabuada} x {c:<2} = {tabuada * c} ')
