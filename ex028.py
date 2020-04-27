from random import randint
escolhido = randint(0,5)
var = int(input('Digite um número de 0 a 5: '))
if var == escolhido:
    print('Parabéns! Você acertou!')
else:
    print('Ah que pena! O número sorteado foi {} ! Tente de novo!' .format(escolhido))