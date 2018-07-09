'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiusculas
o nome com todas minusculas
Quantas letras ao todo(Sem consiserar espaços)
Quantas letras tem o primeiro nome'''


nome = str(input('Nome Completo: ')).strip()

print('Nome em MAIÚSCULAS: {}'.format(nome.upper()))
print('Nome em minusculas: {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))


'''outra maneira'''
separa = nome.split()
print('O seu nome é {} e tem {} letras'.format(separa[0], len(separa[0])))



