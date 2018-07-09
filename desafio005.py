#Faça um programa que leia um numero inteiro e
# mostre na tela o seu sucessore e anrecessor

n = int(input('Digíte um número: '))
a = n - 1
s = n + 1

print('Seu numero: {}\nAntecessor: {} \nSucessor: {}'.format(n, a, s,))
print()

#Outra Forma
print('Seu numero: {}\nAntecessor: {} \nSucessor: {}'.format(n, (n-1), (n+1)))


