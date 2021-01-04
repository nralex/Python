#########################################################################################
# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.              #
#########################################################################################
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
d = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
c = []
for contador in range(0, 10):
    c.append(a[contador])
    c.append(b[contador])
    c.append(d[contador])
print(c)