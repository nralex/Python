'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
lista = []
for c in range(0, 5 ):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        posição = 0
        while posição < len(lista):
            if n <= lista[posição]:
                lista.insert(posição, n)
                print(f'Adicionado na posição {posição} da lista')
                break
            posição += 1
print(f'Os valores digitados em ordem são {lista}')