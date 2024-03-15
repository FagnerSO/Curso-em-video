from time import sleep
from os import system


def desenha_linha(n = 40):
    print('-' * n)
    
def limpa_tela():
    system('cls')
    
def menu_opcao(txt):
    limpa_tela()
    desenha_linha()
    print(f'{txt:^40}')
    desenha_linha()
    
def menu():
    desenha_linha()
    print(f'{"MENU PRINCIAPL":^40}')
    desenha_linha()
    print(f'\033[33m1 - \033[34mVer pessoas cadastradas\033[m')
    print(f'\033[33m2 - \033[34mCadastrar nova pessoa \033[m')
    print(f'\033[33m3 - \033[34mDeletar pessoa cadastrada\033[m')
    print(f'\033[33m4 - \033[34mSair do sistema\033[m')
    desenha_linha()

equipe = []
pessoa = {}

while True:
    menu()
    opcao = int(input('\033[33mSua opção: \033[m'))
    desenha_linha()
    if opcao == 1:
        menu_opcao("PESSOAS CADASTRADAS")
        for i in range(len(equipe)):
            print(f'{equipe[i]["nome"]:<30}{equipe[i]["idade"]} anos')
        sleep(0.5)

    if opcao == 2:
        menu_opcao("NOVO CADASTRO")
        pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
        pessoa['idade'] = int(input('Idade: '))
        pessoa['profissão'] = str(input('Profissão: ')).strip().capitalize()
        equipe.append(pessoa.copy())
        print(f'Registro de {pessoa["nome"]} realizado.')
        sleep(0.5)
    if opcao == 4:
        menu_opcao('Saindo do sistema... Até Logo!')
        break
print(equipe)

