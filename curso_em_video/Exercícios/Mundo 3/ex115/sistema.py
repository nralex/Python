from lib import *
from arquivo import *
from time import sleep

arq = 'cursoEmVídeo.txt'

if not arquivoExiste(arq):
    print('Arquivo não encontrado!')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de criar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2 :
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)