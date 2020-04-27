d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km todados? '))
v = (d * 60) + (km * 0.15)
print('O total a paga é de R${:.2f}' .format(v))
