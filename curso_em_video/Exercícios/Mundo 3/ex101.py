"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL ou OBRIGATÓRIO nas eleições.
"""
def voto(nascimento):
    from datetime import date
    ano = date.today().year
    idade = ano - nascimento
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 18 > idade >= 16 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('-' * 35)
anodeNascimento = int(input('Em que ano você nasceu? '))
print(voto(anodeNascimento))