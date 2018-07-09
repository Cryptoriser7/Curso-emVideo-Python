# Faça um algoritmo que leia o salario de um funcionario
#e mostre seu novo salario cm 15% de aumento


a = input('Nome: ')
b = float(input('Salário de {}: '.format(a)))



print()
print('-' * 70)

print('Parabéns Sr(a). {}, pois o seu salário vai ser aumentado em {:.2f}€\npara o novo valor de {:.2f}€'.format(a, (b * 0.15), (b * 1.15)))
print('-' * 70)



