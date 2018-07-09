'''Faça um prgrama que leia tres numeros e mostre qual e o maior e qual é o menor'''

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))
print()

if n1 < n2 < n3:
    print('Maior: {}\nMenor: {}'.format(n3, n1))
if n1 < n3 < n2:
    print('Maior: {}\nMenor: {}'.format(n2, n1))
if n2 < n1 < n3:
    print('Maior: {}\nMenor: {}'.format(n3, n2))
if n2 < n3 < n1:
    print('Maior: {}\nMenor: {}'.format(n1, n2))
if n3 < n1 < n2:
    print('Maior: {}\nMenor: {}'.format(n2, n3))
if n3 < n2 < n1:
    print('Maior: {}\nMenor: {}'.format(n1, n3))
if n3 == n1 or n3 == n2 or n2 == n1:
    print('Erro! Números iguais')




