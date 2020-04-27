l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
m = l * a
t = m / 2
print('Sua parede tem dimensão {:.2f}x{:.2f} e sua área é de {:.3f} metros quadrados.' .format(l, a, (l * a)))
print('Para pintar essa parede, vocẽ precisará de {}l de tinta.' .format(t))