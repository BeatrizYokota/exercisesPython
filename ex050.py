soma = 0
cont = 0
for c in range (1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números pares e a soma dos números pares digitados é {}' .format(cont, soma))
