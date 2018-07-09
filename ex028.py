'''Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
'''

print('O computador pensou em um número de 0 a 5\nConsegues adivinhar o número?')
import random
l = [1,2,3,4,5]
r = random.choice(l)

print()

n = int(input('Palpite: '))


print()

print('PARABÉNS!!! o número era {}'.format(r) if n == r else 'Tenta novamente. O numero era {}'.format(r))


