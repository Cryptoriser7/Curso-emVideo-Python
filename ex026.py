'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra 'a'
Em que posiçºao ela aparece a primeira vez
Em que posição ela aparece a ultima vez'''


f = str(input('Frase: ')).strip()
x = f.upper()

print('Quantas vezes aparece letra "a": {}'
      .format(x.count('A')))
print('Aparece a primeira vez na posição: {}'
      .format(x.find('A')))
print('Aparece a ultima vez na posição: {}'
      .format(x.rfind('A')))


