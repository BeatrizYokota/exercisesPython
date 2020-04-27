from random import randint
from time import sleep

escolhido = []
jogos = []
cont = 0

print('-'*40)
print('         JOGO DA MEGA SENA     ')
print('-'*40)

n = int(input('Quantos números você deseja sortear: '))
total = 1

while total <= n:
    cont = 0
    while True:
        sorteado = randint(1, 60)
        if sorteado not in escolhido:
            escolhido.append(sorteado)
            cont += 1
        if cont >= 6:
            break
    escolhido.sort()
    jogos.append(escolhido[:])
    escolhido.clear()
    total += 1
print('         SORTEANDO OS NÚMEROS       ')
print('-='*20)
for i, j in enumerate(jogos):
    print(f'Jogo {i}: {j}')
    sleep(1)
print(f'-='*5, '< BOA SORTE! >', f'-='*5)
