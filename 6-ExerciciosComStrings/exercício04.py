#####################################################################################################################
# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.         #
#####################################################################################################################
nome = str(input('Nome: '))
l = []
for c, v in enumerate(nome):
    l.append(v)
    for d, w in enumerate(l):
        if d < len(l) - 1:
            print(w.upper(), end='')
        if d == len(l) - 1:
            print(w.upper())
