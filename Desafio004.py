# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas a informaçoes
# possiveis sobre ele


n = input('Digite algo: ')
x = '-------------'
print()
print()


print('Tipo Primitivo:', type(n))
print(x)
print('Mais informações:')
print()
print('É numério? ', n.isnumeric())
print('É alfabetico? ', n.isalpha())
print('É Alfanumérico? ', n.isalnum())
print('É somente espaços:', n.isspace())
print('Esta em maiusculas?',n.isupper())
print('Esta em minusculas?', n.islower())
print('Esta capitalizada', n.istitle())
print()
print('És o maior, Márcio')
print(x)
