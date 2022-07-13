largura = float(input('Informe a largura: '))
altura = float(input('Infome a altura: '))

area = largura * altura
print('Sua parede tem dimensão de {}x{} e sua área é de {}m2'.format(largura, altura, area))

tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
