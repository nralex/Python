def leiaDinheiro(valor):
    válido = False
    while not válido:
        entrada = str(input(valor)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)
