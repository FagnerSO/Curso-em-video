print(f'\033[44m{" Expressões Matematicas ":=^50}\033[m')

expressao = input('Digite a expressão: ').replace(' ', '').split()
dir = esq = 0
for i in expressao[0]:
    if i == '(':
        dir += 1
    elif i == ')':
        esq += 1
if dir == esq:
    print('Sua expressão é valida!')
else:
    print('Sua expressão é invalida!')

#Solução Guanabara - Inseri '(' em uma lista e a cada aparição do ') ele retira
'''expr = str(input('Digite a expressão: '))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão é invalida!')'''
