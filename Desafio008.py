#Escreva um programa que leia um valor em metros
#e o exiba convertido em centimetros e milimetros

metro = float(input('Valor em Metros: '))
cent = metro*100
mili = cent*10
x = '------------------------'

print(x)
print('{} metros equivalem a:\n{} centímetros \n{} milímetros.'.format(metro, cent, mili))
print(x)
