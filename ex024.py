'''Leia um nome de uma cidade e diga se ela começa ou nao por 'Santo' '''

c = str(input('Nome da Cidade: ')).strip()
print(c[:5].upper() == 'SANTO')


