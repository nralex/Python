teste = list()
teste.append('Alex')
teste.append(35)
galera = list()
galera.append(teste[:])
teste[0] = 'Laura'
teste[1] = 2
galera.append(teste[:])
print(galera)