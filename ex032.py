'''Faça um pograma que leia um ano qualquer e mostre se ele é bissexto'''

ano = int(input('Ano: '))
x = ano % 4

if x == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano Bissexto')
else:
    print('Ano Nao Bissexto')
