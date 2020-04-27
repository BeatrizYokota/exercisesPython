lista = []
maior = menor = 0
for c in range (0,5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    if lista[c] > maior:
        maior = lista[c]
    if lista[c] < menor:
        menor = lista[c]
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(lista):
    if lista[i] == maior:
        print(f'{i}')
print(f'O maior valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(lista):
    if lista[i] == menor:
        print(f'{i}')
