from random import randint

maior = menor = 0

escolhido = []
for c in range(0, 5 ):
    escolhido.append(randint(0, 11))
    if c == 0:
        maior = menor = escolhido[c]

    if escolhido[c] > maior:
        maior = escolhido[c]
    elif escolhido[c] < menor:
        menor = escolhido[c]

print(f'Os números sorteados são: {escolhido}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi; {menor}')
