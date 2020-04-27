from random import randint

sorteados = []

def lista():
    sorteado = 0
    for c in range(0,5):
        sorteado = randint(0,10)
        sorteados.append(sorteado)
    print(f'Sorteando 5 valores da lista: {sorteados} PRONTO!')

def somaPar():
    somaPares = 0
    for c in sorteados:
        if c % 2 == 0:
            somaPares += c
    print(f'Somando os valores pares de {sorteados}, temos {somaPares}')

# PROGRAMA PRINCIPAL
lista()
somaPar()