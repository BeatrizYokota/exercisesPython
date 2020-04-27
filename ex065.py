
continua = 'S'
cont = menor = maior = soma = media = 0

while continua in 'Ss':
    n = float(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    continua = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

media = soma / cont
print('Você digitou {} números e a média foi {}' .format(cont, media))
print('O maior valor foi {} e o menor valor foi {}' .format(maior, menor))