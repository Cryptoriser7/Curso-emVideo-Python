'''Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
ex.:
Digite um numero: 1834
unidade: 4
dezena: 3
Centena: 8
Milhar: 1
'''

n = str(input('digite um numero de 0 a 9999: ')).zfill(4)




print('Unidades {}'.format(n[3]))
print('Dezenas: {}'.format(n[2]))
print('Centenas: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))


