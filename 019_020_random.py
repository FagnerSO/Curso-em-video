from random import choice, sample, shuffle
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

aluno = [a1, a2, a3, a4]

print(f'O aluno será {choice(aluno)}')

print(f'A ordem de apresentação será  {sample(aluno, 4)}')

shuffle(aluno)
print(f'A ordem de apresentação será  {aluno}')