#################################################################
# Faça um programa que leia um nome de usuário e a sua senha    #
# e não aceite a senha igual ao nome do usuário, mostrando      #
# uma mensagem de erro e voltando a pedir as informações.       #
#################################################################
while True:
    usuário = str(input('Usuário: '))
    senha = str(input('Senha: '))
    if usuário != senha:
        break
    print('\033[31mERRO! Informe usuário e senha\033[m')