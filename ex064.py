soma = cont = 0
n = float(input('Digite um número [999 para parar]: '))

while n != 999:
    n = float(input('Digite um número [999 para parar]: '))
    soma += n
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}' .format(cont, soma))
