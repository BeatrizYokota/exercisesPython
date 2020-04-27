num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print("O maior valor é {} e o menor valor é {}" .format(num1, num2))
elif num2 > num1:
    print("O maior valor é {} e o menor valor é {}".format(num2, num1))
else:
    print("Não existe maior e menor valor, os dois valores são iguais!")
