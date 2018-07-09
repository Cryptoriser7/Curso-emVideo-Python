#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome escolhido

import random
a1 = input('Aluno A: ')
a2 = input('Aluno B: ')
a3 = input('Aluno C: ')
a4 = input('Aluno D: ')
x = [a1, a2, a3, a4]
z = random.choice(x)
print()

print('Aluno: {}'.format(z))

'''Para criar uma lista de variaveis ou grupo de variaveis, neste exemplo, criamos uma nova variavel e
colocamos as variaveis que queremos no grupo dentro de parentises retos [].
Para sortear variaveis, usa-se random.choice(x).
Neste ex. era recomendado usar input denominado de string str(input())nas variaveis referentes aos nomes'''




