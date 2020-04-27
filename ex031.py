distancia = float(input('Digite a distância da viagem: '))
if distancia <= 200 :
    valor = distancia * 0.50
    print('O preço da passagem é {} reais' .format(valor))
else:
    valor = distancia * 0.45
    print('O preço da passagem é {} reais'.format(valor))
