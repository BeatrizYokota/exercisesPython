print('=' *30)
print('BANCO CEV')
print('=' *30)

valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
ced = 50
totalCedula = 0

while True:
    if total >= ced:
        total -= ced
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCedula = 0
        if total == 0:
            break
