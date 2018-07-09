#Crie um programa que leia um numero real qualquer pelo teclado e mostre a sua porção inteira
# ex: Digite o numero 6.127. O número 6.127 tem a parte inteira 6.

from math import floor

print()
n = float(input('Digite um número: '))
print()
print('.' * 20)
print('Parte inteira: ', floor(n))
print('.' * 20)

print('By Jaiuu')
