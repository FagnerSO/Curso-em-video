import emoji
from random import choice
from time import sleep

print('#'*15, '\033[7:33mJOKEN-PÔ\033[m', '#'*15)
print('Suas Opções\n'
      '[0] Pedra\n'
      '[1] Papel\n'
      '[2] Tesoura\n')

jogador = int(input('Qual a sua Jogada: '))
papel = emoji.emojize(':raised_hand:')
tesoura = emoji.emojize(':victory_hand:')
pedra = emoji.emojize(':oncoming_fist:')
jogo = [papel, tesoura, pedra]
pc = choice(jogo)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!\n')

if jogador == 0 and pc == tesoura:
    print('Jogador ',pedra, ' x ', pc, 'PC')
    print('!!!PARABÉNS VOCE VENCEU!!!')
elif jogador == 1 and pc == pedra:
    print('Jogador ', papel, ' x ', pc, 'PC')
    print('!!!PARABÉNS VOCE VENCEU!!!')
elif jogador == 2 and pc == papel:
    print('Jogador ', tesoura, ' x ', pc, 'PC')
    print('!!!PARABÉNS VOCE VENCEU!!!')
elif jogador == pc:
    print('Empate')
else:
    print('Voce perdeu, tente novamente!!')

print('PC', pc, '\n')