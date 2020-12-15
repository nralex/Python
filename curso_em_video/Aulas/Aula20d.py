def dobra(lista):
    posição = 0
    while posição < len(lista):
        lista[posição] *= 2
        posição += 1


valores = [1, 2, 3, 4, 5, 6]
dobra(valores)
print(valores)