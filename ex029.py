'''Escreva um programa que leia a velocidade de um carro.
Se ele ultruapassar os 80kh/h, mostre uma mensagens dizendo que ele foi multado
A multa vai custar 7,00 por cada km acima do limite'''

velocidade = int(input('Velocidade: km/h '))
multa = (velocidade - 80) * 7.00
D = velocidade - 80
print()


if velocidade >= 80:
    print('Você excedeu o limite de 80 km/h, atingindo a velocidade de {} km/h, mais {} km/h do que é permitido.\nDe acordo com a taxa atual, a sua multa será {:.2f} Euros'.format(velocidade,D,multa))
else:
    print('Você nao excedeu o limite de velocidade. Vá á sua vida!')
