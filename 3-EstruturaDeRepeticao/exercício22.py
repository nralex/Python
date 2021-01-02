#############################################################################################
# Altere o programa de cálculo dos números primos, informando, caso o número não seja       #
# primo, por quais número ele é divisível.                                                  #
#############################################################################################
n = int(input('Digite um número: '))
para_comparar = [1, n]
divisível_por = []
for c in range(1, n + 1):
    if n % c == int():
        divisível_por.append(c)
if divisível_por == para_comparar:
    print(f'{n} é um número primo.')
elif n == 1:
    print(f'{n} é um número primo.')
else:
    print(f'Como {n} é divisível por {divisível_por}, {n} não é um número primo.')
print('Um número primo é aquele que é divisível somente por ele mesmo e por 1')
