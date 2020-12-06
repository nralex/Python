''' Crie uma tupla preencida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de classificação.
Depois mostre:
a) Apenas os 5 primeiros colocados;
b) Os últimos 4 colocados da tabéla;
c) Uma lista com os times  em ordem alfabética;
d) Em que posição na tabela está o time da Chapecoense.
'''
t = ('Atlético', 'São Paulo', 'Flamengo', 'Internacional', 'Palmeiras', 'Santos',
 'Grêmio', 'Fluminense', 'Fortaleza', 'Corinthians', 'Ceará', 'Athletico Paranaense', 
 'Bahia', 'Atlético-GO', 'Red Bull Bragantino', 'Sport', 'Vasco da Gama', 'Coritiba', 'Botafogo', 'Goiás')
print('-=' * 30)
print(f'Lista de times do brasileirão: {t}')
print('-=' * 30)
print(f'Os 5 primeiros são {t[0:5]}')
print('-=' * 30)
print(f'Os 4 últimos são {t[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(t)}')
print('-=' * 30)
print(f'O Ceará está na {t.index("Ceará") + 1}ª posição.')
print('-=' * 30)