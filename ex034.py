'''Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
para salarios suoperiores a 1.250,00, calcule um aumento em 10%
para os inferiores ou iguais, o  aumento é de 15%'''

salario = float(input('Salario: '))

a1 = salario * .15
a2 = salario * .10

if salario <=1250.00:
    print('O seu salario de {:.2f} euros é inferior a 1,250.00 €,\nportanto terá um aumento de 15% no valor de {:.2f} euros'.format(salario, a1))
else:
    print('O seu salario de {:.2f} euros é superior a 1,250.00 €,\nportanto terá um aumento de 10% no valor de {:.2f} euros'.format(salario, a2))
