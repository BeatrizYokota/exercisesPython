n = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
decimo = n + (10 - 1) * r
for c in range (n, decimo + r, r):
    print('{}' .format(c), end = ' ->  ')
print('Acabou!')
