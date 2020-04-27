print('-' *20)
print('SEQUÊNCIA DE FIBONACCI')
print('-' *20)

n1 = 0
n2 = 1
total = 0
n = int(input('Digite um número: '))

print('{} -> {}' .format(n1, n2), end = '')
cont = 3
while cont <= n:
    total = n1 + n2
    n1 = n2
    n2 = total
    print(' -> {}' .format(total), end = '')
    cont += 1
print(' -> FIM')