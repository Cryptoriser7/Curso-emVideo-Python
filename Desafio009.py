#Faça um programa que leia um numero inteiro qualquer
#e mostre na tela a sua tabuada

nu = int(input('Tabuada dos: '))
x = '---------------'
a = nu*1
b = nu*2
c = nu*3
d = nu*4
e = nu*5
f = nu*6
g = nu*7
h = nu*8
i = nu*9
j = nu*10

print()

print(x)

print('Tabuada dos',nu)
print(nu, 'x  1  =', a)
print(nu, 'x  2  =', b)
print(nu, 'x  3  =', c)
print(nu, 'x  4  =', d)
print(nu, 'x  5  =', e)
print(nu, 'x  6  =', f)
print(nu, 'x  7  =', g)
print(nu, 'x  8  =', h)
print(nu, 'x  9  =', i)
print(nu, 'x 10  =', j)
print(x)


print('{} x {:2} = {}'.format(nu, 1, nu*1))
print('{} x {:2} = {}'.format(nu, 2, nu*2))
print('{} x {:2} = {}'.format(nu, 3, nu*3))
print('{} x {:2} = {}'.format(nu, 4, nu*4))
print('{} x {:2} = {}'.format(nu, 5, nu*5))
print('{} x {:2} = {}'.format(nu, 6, nu*6))
print('{} x {:2} = {}'.format(nu, 7, nu*7))
print('{} x {:2} = {}'.format(nu, 8, nu*8))
print('{} x {:2} = {}'.format(nu, 9, nu*9))
print('{} x {} = {}'.format(nu, 10, nu*10))

print('-' *12)



z = bool(input('Press any key to exit'))
exit()
