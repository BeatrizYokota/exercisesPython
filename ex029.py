v = float(input('Digite a velocidade autal do carro: '))
if v > 80:
    multa = (v - 80)*7
    print('MULTADO! Você ultrapassou  o limite que é de 80km/h. A multa é de {} reais' .format(multa))