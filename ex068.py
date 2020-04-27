from random import randint

v = soma = 0


print('-='*30)
while True:
    print('VAMOS JOGAR PAR OU IMPAR')
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou impar?[P/I] ')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador {computador}. O total é {soma}')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')