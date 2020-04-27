fat = 1
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
print('Calculando {}! = ' .format(n), end='')
while c > 0:
    print('{}' .format(c), end ='')
    print(' x ' if c > 1 else ' = ', end = '')
    fat *= c
    c -= 1
print('{}' .format(fat))
