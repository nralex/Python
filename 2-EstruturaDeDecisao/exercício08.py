# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

preços = {}
for c in range(1, 4):
    preços[float(input(f'Digite o {c}° preço: R$'))] = (c)  # Inverti o raciocínio: coloquei o preço como chave e o n° do produto como valor.
print(f'O {preços[min(preços)]}° produto é o mais barato (R${min(preços):.2f})')
