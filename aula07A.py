#nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um Valor: '))
n2 = int(input('Outro Valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
e = n1**n2
di = n1//n2


print('A soma vale {},\na multiplicação {}, a divisão {:.3f}\ne o exponencial vale {}'.format(s, m, d, e))
print('Divisão inteira é {} '.format(di))


