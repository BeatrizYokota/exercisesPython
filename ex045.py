from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
escolhido = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
num = int(input('Qual a sua jogada? '))
print('O computador jogou {}' .format(itens[escolhido]))
print('Jogador escolheu {}' .format(itens[num]))
if escolhido == 0:
    if num == 0:
        print('Empate!')
    elif num == 1:
        print('Você ganhou!')
    elif num == 2:
        print('Você perdeu!')
    else:
        print('Jogada inválida!')
elif escolhido == 1:
    if num == 0:
        print('Você perdeu!')
    elif num == 1:
        print('Empate!')
    elif num == 2:
        print('Você ganhou!')
    else:
        print('Jogada inválida!')
elif escolhido == 2:
    if num == 0:
        print('Você ganhou!!')
    elif num == 1:
        print('Você perdeu!')
    elif num == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')
