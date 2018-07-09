'''Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome separadamente
ex.: Ana Maria de Souza
primeiro: ana
ulrimo: Souza'''

n = str(input('Nome Completo: ')).strip()
t = n.title()
s = t.split()



print('Primeiro nome: {}\nUltimo nome: {}'
      .format(s[0], s[-1]))


'''fiz isto sem ver a resolução, nem sei como xDD'''

