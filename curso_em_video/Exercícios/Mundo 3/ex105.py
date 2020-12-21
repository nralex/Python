"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

- Quantidade de notas;
- A maior nota;
- A menor nota;
- A média da turma;
- A situação (opcional).

Adicione também as docstrings da função.
"""
def notas(*num, sit=False):
    """
    notas(*num, sit=False)
        -> Função para analizar notas e situação de vários alunos.
        :parametro num: uma ou mais notas dos alunos (aceita vários)
        :parametro sit: valor opcional, indicando se deve ou não mostrar a situação.
        :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionário = dict()
    dicionário['total'] = len(num)
    dicionário['maior'] = max(num)
    dicionário['menor'] = min(num)
    med = sum(num) / len(num)
    dicionário['média'] = med
    if sit:
        if med < 5:
            situação = 'RUIM'
        if 5 <= med < 7:
            situação = 'RAZOÁVEL'
        if med >= 7:
            situação = 'BOA'
        dicionário['situação'] = situação
    return dicionário


resposta = notas(5.5, 2.5, 10, 6.5, sit = False)
print(resposta)
help(notas)