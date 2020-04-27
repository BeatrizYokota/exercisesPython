pesoMenor = 0
pesoMaior = 0
for c in range (1,6):
    peso = float(input('Peso da {}º pessoa: ' .format(c)))
    if c == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print('O maior peso lido foi {}Kg' .format(pesoMaior))
print('O menor peso liso foi {}Kg' .format(pesoMenor))
