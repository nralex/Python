#####################################################################################################################
# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo   #
# um relatório dos endereços IP válidos e inválidos.                                                                #
#####################################################################################################################
def verificaIp(ip): 
    """Retorna se um IP é valido ou não."""
    ip = ip.split('.')
    for c in range(len(ip)):
        if int(ip[c]) > 255:
            return False
    return True


arquivo = open(r'7-ExerciciosArquivos\IPs.txt') # Abre o arquivo
endereços = arquivo.readlines() # transforma e ua lista
for i in range(len(endereços)):
    endereços[i] = endereços[i].rstrip('\n') # Retira a quebra de linha
arquivo.close() # Fecha o arquivo
válido = []
inválido = []
for c in range(len(endereços)): #Verifica os IPs guardados na variável endereços
    if verificaIp(endereços[c]):
        válido.append(endereços[c]) # Guarda os IPs válidos na lista válido.
    else:
        inválido.append(endereços[c]) # Guarda os IPs inválidos na lista inválido.

relatório = open(r'7-ExerciciosArquivos\RelatórioDeIps.txt', 'w', encoding='utf-8') #Abre, ou cria o arquivo para escrita, coloquei utf-8 para escrever todos os caracteres normalmente.
relatório.write('Endereços de IP válidos:\n')
for i, v in enumerate(válido):
    relatório.write(f'{v}\n')
relatório.write('\nEndereços de IP inválidos:\n')
for i, v in enumerate(inválido):
    relatório.write(f'{v}\n')
relatório.close()