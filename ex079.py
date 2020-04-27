import time

lista = []
resposta = 0

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado')
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'Nn':
        break
lista.sort()
print(f'{lista}')
