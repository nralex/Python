#############################################################################################
# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais #
# baixo, o mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a  #
# cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação  #
# de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o   #
# programa também deve ser informados os códigos e valores do cliente mais alto, do mais    #
# baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes  #
#############################################################################################
código_alto = alto = código_baixo = baixo = código_gordo = gordo = código_magro = magro = 0
total_altura = total_peso = 0
contador = 1
while True:
    # Pergunta código
    código = int(input('Código: [0 para sair] '))
    # O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
    if código == 0:
        break
    # Pergunta altura
    altura = int(input('Altura: [cm] '))
    # Pergunta peso
    peso = float(input('Peso: [kg] '))
    # Informa os códigos e valores do cliente mais alto
    if altura > alto:
        alto = altura
        código_alto = código
    # Informa os códigos e valores do cliente mais baixo
    if baixo == 0:
        baixo = altura
        código_baixo = código
    if altura < baixo:
        baixo = altura
        código_baixo = código    
    # Informa os códigos e valores do cliente mais gordo
    if peso > gordo:
        gordo = peso
        código_gordo = código
    # Informa os códigos e valores do cliente mais magro
    if magro == 0:
        magro = altura
        código_magro = código
    if peso < magro:
        magro = altura
        código_magro = código
    # Informa a média das alturas dos clientes
    contador += 1
    total_altura += altura
    média_altura = total_altura / contador
    # Informa a média dos pesos dos clientes
    total_peso += peso
    média_peso = total_peso / contador
print(f"""Cliente mais alto {código_alto} com {alto}cm
Cliente mais baixo {código_baixo} com {baixo}cm
Cliente mais gordo {código_gordo} com {gordo}kg
Cliente mais magro {código_magro} com {magro}kg
A média da altura dos clientes é {média_altura:.1f}cm
A média do peso dos clientes é {média_peso:.1f}kg""")
