#############################################################################################
# O cardápio de uma lanchonete é o seguinte:                                                #
#       Especificação   Código  Preço                                                       #
#       Cachorro Quente 100     R$ 1,20                                                     #
#       Bauru Simples   101     R$ 1,30                                                     #
#       Bauru com ovo   102     R$ 1,50                                                     #
#       Hambúrguer      103     R$ 1,20                                                     #
#       Cheeseburguer   104     R$ 1,30                                                     #
#       Refrigerante    105     R$ 1,00                                                     #
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.          #
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do      #
# pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.         #
#############################################################################################
print('-' * 50)
print(f'{"CARDÁPIO":^50}')
print('-' * 50)
produtos = {
    100 : ['Cachorro Quente', 1.20], 
    101 : ['Bauru Simples', 1.3],
    102 : ['Bauru com ovo', 1.5],
    103 : ['Hambúrguer', 1.2],
    104 : ['Cheeseburguer', 1.3],
    105 : ['Refrigerante', 1]}
print('-' * 50)
for i, (k, v) in enumerate(produtos.items()):
    print(f'{v[0]:.<32}: cod.:{k} R$ {v[1]:4.2f}')
vendido = {}
while True:
    try:
        escolha = int(input('Letras para sair\nInsira o código do lanche desejado: '))
        print('-' * 50)
    except:
        print('Obrigado! Volte sempre!')        
        break
    else:
        if 100 <= escolha <= 105:            
            quantidade = int(input('Quantos deseja? '))
            vendido[produtos[escolha][0]] = [quantidade, produtos[escolha][1], produtos[escolha][1] * quantidade]
            print('-' * 50)
        else:            
            print(print('Obrigado! Volte sempre!'))
            break
contador = 1
total = 0
print('-' * 50)
for i, (k, v) in enumerate(vendido.items()):
    print(f'{contador:<3} - {k:16} : {v[0]:>3} * R$ {v[1]:4.2f} = R$ {v[2]:6.2f} ')
    contador += 1
    total +=v[2]
if total > 0:
    print('-' * 50)
    print(f'Total = R$ {total:.2f}')
    print('-' * 50)
