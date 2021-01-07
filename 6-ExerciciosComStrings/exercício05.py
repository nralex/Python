#####################################################################################################################
# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.             #
#####################################################################################################################
nome = 'fulano'
for c in range(0, len(nome)):
    if c == 0:
        print(nome.upper())
    else:
        print(nome[:-c].upper())
    
