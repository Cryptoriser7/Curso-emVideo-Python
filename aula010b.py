'''nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que lindo nome voce tem!')
print('Bom dia, {}!'.format (nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunta nota: '))
m = (n1 +n2)/2
print('A sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua media foi boa!PARABÈNS!')
else:
    print('Sua media foi rui! ESTUDE MAIS')
