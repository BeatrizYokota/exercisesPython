cont = total = menorPreco = maiorPreco = 0
produtoMaisBarato = ' '

print('-' *30)
print('LOJA SUPER BARATÃO')
print('-' *30)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    cont += 1

    if preco >= 1000:
        maiorPreco += 1

    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        produtoMaisBarato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break
print(f'O total da compra foi {total}')
print(f'Foram {maiorPreco} produtos comprados no valor acima de mil reais')
print(f'O produto mais barato foi {produtoMaisBarato} que custou apenas {menorPreco}')
