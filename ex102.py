from math import factorial

def fatorial(n, show):
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    print(f)


# Programa Principal
num = int(input('Digite um número: '))
print(factorial(num))
while True:
    resp = str(input('Deseja mostrar o cálculo? [S/N] ')).strip().upper()[0]
    if resp== 'N':
        break
    elif resp == 'S':
        resp = True
        fatorial(num, resp)
        break
