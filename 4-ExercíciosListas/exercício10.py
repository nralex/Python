#########################################################################################
# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor  #
# de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos #
# dois outros vetores.                                                                  #
#########################################################################################
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
c = []
for contador in range(0, 10):
    c.append(a[contador])
    c.append(b[contador])
print(c)