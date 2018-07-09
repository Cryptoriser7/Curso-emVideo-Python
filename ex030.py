'''Crie um programa que leia um numero inteiro qualquer e mostre na tela se ele é par ou impar'''

n = int(input('Digite um numero: '))
x = n % 2
print()
if x == 1:
    print('Numero Impar')
else:
    print('Numero Par')
