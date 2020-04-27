lista = [[],[]]
valor = 0

for n in range(1,8):
    valor = int(input(f'Digite o {n}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 == 1:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Todos os valores PARES: {lista[0]}')
print(f'Todos os valores ÍMPARES: {lista[1]}')
