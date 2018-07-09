'''Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem,
cobrando 0,50 por km para viagens ate 200 km e 0.45 para viagens mais longas'''

distancia = int(input('Digite a distancia em km: '))
ta = distancia * 0.5
tb = distancia * 0.45

if distancia >= 200:
    print('O preço da sua viagem para {} km será {:.2f} euros. Pagará 0.45 €/km'.format(distancia, tb))
else:
    print('O preço da sua viagem para {} km será {:.2f} euros. Pagará 0.50 €/km'.format(distancia, ta))

