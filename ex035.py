'''desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.'''

a = float(input('comprimento 1: '))
b = float(input('Comprimento 2: '))
c = float(input('Comprimento 3: '))
print()

if b - c < a < b + c and a - c < b < a + b and a - b < c < a + b:
    print('Pode-se formar um triangulo')
else:
    print('Não se pode formar um triangulo')
