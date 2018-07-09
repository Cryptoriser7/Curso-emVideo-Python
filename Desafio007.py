#Desenvolva um programa que leia as duas notas de um
# aluno, calcule e mostre a sua media

aluno = input('Aluno: ')
n1 = float(input('Nota A: '))
n2 = float(input('Nota B: '))
s = n1+n2
m = s/2
x = '--------------------------------------'

print(x)
print('Valor médio de {} é {:.1f} valores'.format(aluno, m))
print(x)

