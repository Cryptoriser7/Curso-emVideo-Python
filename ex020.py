# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada


from random import shuffle
a = str(input('aluno A: '))
b = str(input('Aluno B: '))
c = str(input('Aluno C: '))
d = str(input('Aluno D: '))
x = [a, b, c, d]
shuffle(x)

print('Ordem dos alunos: ')
print(x)

'''random.shuffle(x) nao precisa de ser uma variavel'''