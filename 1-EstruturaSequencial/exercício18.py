# Faça um programa que peça o tamanho de um arquivo para download (em MB) 
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
# aproximado de download do arquivo usando este link (em minutos).
tamanho = float(input('Informe o tamanho do arquivo: [MB] '))
velocidade = float(input('Informe a velocidade da sua internet: [Mbps] '))
minutos = ((tamanho * 1024) / ((velocidade * 1024) /8)) // 60
segundos = ((tamanho * 1024) / ((velocidade * 1024) /8)) % 60
print(f'Tempo: {minutos} minutos e {segundos} segundos')