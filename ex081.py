lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'Nn':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Osvalores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista')
