def notas(*n, sit=False):
    """
    Função para analisar notas de alunos
    :param n: uma ou mais notas ds alunos
    :param sit: (valor opcional) indica situção em relação a média
    :return: dicionario com varias informações sobre a situação da turma
    """
    aluno = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': sum(n) / len(n)}
    if sit:
        if aluno['média'] >= 7:
            aluno['situação'] = 'BOA'
        elif 5 <= aluno['média'] < 7:
            aluno['situação'] = 'REGULAR'
        else:
            aluno['situação'] = 'RUIM'

    return aluno

resp = notas(5.5, 0, 0, 6.5, sit=True)
print(resp)
help(notas)