nome = input('Digite seu nome: ').strip()
espaco = nome.replace(' ','')
lista = (nome.split())

print(f'Analisando o nome: {nome}')
print(nome.upper())
print(nome.lower())
print(f'O total de caracteres sem espaço é {len(espaco)}')
print(f'Seu primeiro nome tem {len(lista[0])} letras')