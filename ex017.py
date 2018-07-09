#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# retangulo, calcule e mostre o comprimento da hipotenusa

from math import hypot
print()
x = float(input('Cateto Adjacente: '))
y = float(input('Cateto Oposto: '))
print()
print('-' * 20)
print('Hipotenusa: {:.2f}'.format(hypot(x, y)))
print('-' * 20)

'''
x = float(input('Cateto Adjacente: '))
y = float(input('Cateto Oposto : '))
h = (x ** 2 + y ** 2) ** (1/2)

print('Hipotnusa: {:.2f}'.format(h))'''
