matriz = [[0,0,0],[0,0,0],[0,0,0]]

somaPares = somaTerceiraColuna = maiorValor = 0

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = float(input(f'Digite o valor para a posição [{i}][{j}]: '))
        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]
        if j == 2:
            somaTerceiraColuna += matriz[i][2]
        if i == 1:
            if j == 0:
                maiorValor = matriz[1][0]
            elif matriz[1][j] > maiorValor:
                maiorValor = matriz[1][j]
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}')
print(f'O maior valor da terceira coluna é {maiorValor}')