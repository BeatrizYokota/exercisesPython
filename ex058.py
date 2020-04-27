from random import randint
escolhido = randint(0,11)
cont = 0
num = int(input('Digite um número de 0 a 10: '))
while num != escolhido:
    num = int(input('ERROU, tente de novo: '))
    cont += 1
print('ACERTOU! O número sorteado é {}! Você precisou {} vezes para acertar' .format(escolhido, cont))