#####################################################################################################################
# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo   #
# um relatório dos endereços IP válidos e inválidos.                                                                #
#####################################################################################################################
def verificaIP(ip):
    ''' Verifica somente se os blocos do endereço estão entre 0 e 255 '''
    blocos = str(ip).split('.')
    if len(blocos)!=4:
        return False
    for i in blocos:
        sub_bloco = int(i)
        if sub_bloco<0 or sub_bloco>255:
            return False
    return True

#Abrindo arquivo
arquivo = open("7-ExerciciosArquivos\IPs.txt")
endereços = arquivo.readlines()

#Retira \n de cada palavra
for i in range(len(endereços)):
    endereços[i]=endereços[i].rstrip('\n')
    
#Fecha arquivo
arquivo.close()

#Chama função que classifica endereços
validos = []
inválidos = []
for i in endereços:
    if verificaIP(i):
        validos.append(i)
    else:
        inválidos.append(i)

#Cria arquivo, grava resultados e fecha arquivo
saída = open('7-ExerciciosArquivos\Resultados_IPs.txt', 'w', encoding='utf-8')

saída.write("[Endereços válidos:]\n")
for i in validos:
    saída.write("{}\n".format(i))
    
saída.write("\n[Endereços inválidos:]\n")
for i in inválidos:   
    saída.write("{}\n".format(i))
    
saída.close()

