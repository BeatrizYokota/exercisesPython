a = float(input('Digite a medida da primeira reta: '))
b = float(input('Digite a medida da segunda reta: '))
c = float(input('Digite a medida da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('É possível fazer um triângulo')
    if a == b == c:
        print("Triângulo equilátero!")
    elif a != b != c != a:
        print("Triângulo escaleno!")
    else:
        print("Triângulo isóceles!")
else:
    print('Não é possivel formar um triângulo')
