#####################################################################################################################
# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.#
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e #
# identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu      #
# gerar o seguinte arquivo, chamado "usuarios.txt":                                                                 #
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que    #
# gere um relatório, chamado "relatório.txt", no seguinte formato:                                                  #
#####################################################################################################################
arquivo = open('7-ExerciciosArquivos\\usuários.txt', 'r')
linhas = []
for c in arquivo:
    c = c.split()
    linhas.append(c)
arquivo.close()
total = 0
for c in linhas:
    c[1] = (float(c[1]) * 0.95367432) / 10**6
    total += c[1]
print('''
ACME Inc.               Uso do espaço em disco pelos usuários
-------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso\n''')
for i, v in enumerate(linhas):
    print(f'{i+1:<5}{v[0]:15}{v[1]:13.2f} MB {(v[1] / total) * 100:>11.2f}%')
print(f'\nEspaço total ocupado: {total:.2f} MB')
print(f'Espaço médio ocupado: {total/len(linhas):.2f} MB\n')

