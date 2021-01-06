#####################################################################################################################
# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve     #
# converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para      #
# fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para      #
# P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.         #
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que     #
# desejar.                                                                                                          #
#####################################################################################################################
def converteHora(hora, minutos):
    while True:
        if 0 < hora > 23 or 0 <= minutos >= 59 :
            print('\033[31mErro! Hora inválida!\033[m') 
            hora = int(input('\nDigite as horas para conversão: '))
            minutos = int(input('Digite os minutos para conversão: '))
        else:
            break
    if hora <= 12:
        h = hora
        final = 'AM'
    else:
        h = hora - 12
        final = 'PM'
    return f'Hora convertida: {h:02}:{minutos:02} {final}'


while True:
        h = int(input('Digite as horas para conversão: '))
        m = int(input('Digite os minutos para conversão: '))
        print(converteHora(h, m))
        pergunta = str(input('Deseja continuar? [S para SIM ou qualquer outro carácter para encerrar] ')).upper().strip()[0]
        if pergunta == 'N':
            print('FIM')
            break
