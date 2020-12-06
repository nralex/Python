n =  [2, 5, 9, 1]
n[2] = 3
n.append(7)
n.sort(reverse=True)
n.insert(2,2)
#n.pop(2)
if 5 in n:
    n.remove(5)
else:
    print('Não achei o n° 4')
print(n)
print(f'Essa lista tem {len(n)} elementos.')