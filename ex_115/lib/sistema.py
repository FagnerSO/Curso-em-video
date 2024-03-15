from ex_115.lib.interface import *
from ex_115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

verifica_arquivo(arq)

while True:
    resp = menu(['Ver pessoa cadastrada', 'Cadastrar nova pessoa', 'Deletar pessoa cadastrada', 'Sair do sistema'])
    if resp == 1:
        cabecalho('PESSOAS CADASTRADAS')
        ler_arquivo(arq)
    elif resp == 2:
        cabecalho('CADASTRO NOVO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        inserir_dados_arquivo(arq, nome, idade)
    elif resp == 3:
        cabecalho('DELETAR PESSOA')
        nome = str(input('Nome: '))
        deletar_dados_por_nome(arq, nome)
    elif resp == 4:
        print('Saindo do sistema... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida"\033[m')
    sleep(1)


