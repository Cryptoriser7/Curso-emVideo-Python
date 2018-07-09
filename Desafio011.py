#Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua area e a quantidade de tinta
# necessaria para pinta-la, sabendo que cada litro de tinta pinta
# 2m2


alt = float(input('Altura da sala: '))
lar = float(input('Largura da sala: '))
mq = alt * lar
lt = mq / 2
x = '------------'

print()
print(x)
print('Metros Quadrados da parede: {:.4f} m2\nLitros de Tinta: {:.4f} lts'.format (mq, lt))
print(x)


