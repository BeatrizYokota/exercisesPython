a = float(input('Digite a medida da primeira reta: '))
b = float(input('Digite a medida da segunda reta: '))
c = float(input('Digite a medida da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('É possível fazer um triângulo')
else:
    print('Não é possivel formar um triângulo')