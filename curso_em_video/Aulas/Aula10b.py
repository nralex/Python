n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda média: '))
m = (n1 + n2)/2
print(f'A sua media foi {m:.1f}')
if m < 6:
    print('Se esforce para melhorar esta nota!')
else:
    print('Muito bem continue assim!')
