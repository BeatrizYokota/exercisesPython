def area(larg, comp):
    a = 0
    a = larg * comp
    print(f'A área de um terreno {larg}m x {comp}m é de {a}m²')


# PROGRAMA PRINCIPAL
print()
print('  Controle de Terrenos')
print('-'*25)
x = float(input('LARGURA (m): '))
y = float(input('COMPRIMENTO (m): '))
area(x, y)
