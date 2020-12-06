# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando dados em forma tabular.
pp = ('Alface (1 unidade)', 2.79, 'Cebolas (1kg)', 4.40, 'Batatas (1 kg)', 4.30, 'Tomates (1 kg)', 
5.70,'Laranjas (1 kg)', 4.20, 'Bananas (1kg)', 4.40, 'Maçãs (1 kg)', 7.10, 'Queijo fresco (1 kg)', 30.30, 'Uma dúzia de ovos', 
7.00, 'Arroz (1 kg)', 4.20, 'Um quilo de pão (1 kg)', 6.00, 'Leite (1 litro)',3.70)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for item in range(0, (len(pp))):
    if item % 2 == 0:
        print(f'{pp[item]:.<32}', end='')
    else:
        print(f'R${pp[item]:>6.2f}')
print('-' * 40)
