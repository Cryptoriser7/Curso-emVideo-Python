# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

a = float(input('Ângulo: '))
from math import tan, cos, sin, radians
x = radians(a)
print('Coseno: {:.3f}, Seno: {:.3f}, Tangente: {:.3f}'.format(cos(x), sin(x), tan(x)))

'''Para utilizar as formulas cos; sin; e tan, é necessario que (x) esteja convertido em radianos
Para tal, x = radians de angulo (a)''
'
