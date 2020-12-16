def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


número = int(input('Deigite um número: '))
print(par(número))

if par(número):
    print('É par!')
else:
    print('Não é par!')