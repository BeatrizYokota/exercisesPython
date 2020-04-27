from math import radians, sin, cos, tan
a = float(input('Digite o valor de um ângulo: '))
seno = sin(radians(a))
print('O valor de seno de {} é {:.2f}'. format(a, seno))
cosseno = cos(radians(a))
print('O valor de cosseno de {} é {:.2f}'. format(a, cosseno))
tangente = tan(radians(a))
print('O valor de tangente de {} é {:.2f}'. format(a, tangente))
