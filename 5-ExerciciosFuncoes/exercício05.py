#####################################################################################################################
# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é  #
# a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.     #
# A função “altera” o valor de custo para incluir o imposto sobre vendas.                                           #
#####################################################################################################################
def somaImposto(taxaImposto, custo):
    comImpostos = ((taxaImposto / 100) + 1) * custo
    return comImpostos


taxa = float(input('Imposto: % '))
preço = float(input('Custo [sem impostos]: R$ '))
print(f'Custo com impostos: R$ {somaImposto(taxa, preço):.2f}')