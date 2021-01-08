#####################################################################################################################
# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo   #
# um relatório dos endereços IP válidos e inválidos.                                                                #
#####################################################################################################################
arquivo = open(r'7-ExerciciosArquivos\IPs.txt') # Abre o arquivo
endereços = arquivo.readlines() # transforma e ua lista
for i in range(len(endereços)):
    endereços[i] = endereços[i].rstrip('\n') # Retira a quebra de linha
arquivo.close() # Fecha o arquivo
