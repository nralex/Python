nomcom = input('Digite o seu nome completo: ').strip()
nomlist = nomcom.split()
primnom = nomlist[0]
semesp = nomcom.replace(' ','')
#O nome com todas a letras maiúsculas.
print(f'O seu nome em letras maúsculas fica assim:\n{nomcom.upper()}\n')
#o nome com todas a letras minúsculas.
print(f'O seu nome em letras minúsculas fica assim:\n{nomcom.lower()}\n')
#Quantas letras ao todo (sem considerar os espaços).
print(f'seu nome completo possui {len(semesp)} caracteres, sem contar os espaços.\n')
#quantas letras tem o primeiro nome).
print(f'Seu primeiro nome possui {len(primnom)} letras\n')