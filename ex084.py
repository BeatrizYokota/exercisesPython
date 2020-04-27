pessoa = []
lista = []

maior = menor = 0

while True:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(float(input('Digite o peso: ')))
    if len(lista) == 0:
        maior = menor = pessoa[1]
    elif pessoa[1] > maior:
        maior = pessoa[1]
    elif pessoa[1] < menor :
        menor = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'Nn':
        break
print(f'O total de pessoas cadastradas foram: {len(lista)}')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}] ', end ='')
print(f'\n O menor peso foi de {menor}Kg. Peso de ', end ='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')