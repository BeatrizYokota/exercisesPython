from math import hypot
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hi = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}' .format(hi))
