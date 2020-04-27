lista = []
pares = []
impares = []

while True:
    n =int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    if n % 2 == 1:
        impares.append(n)

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'Nn':
        break
print(f'A lista completa é {lista}')
pares.sort()
print(f'A lista de pares é {pares}')
impares.sort()
print(f'A lista de ímpares é {impares}')
