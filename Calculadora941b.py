from time import sleep


sleep(0.5)
print('-=' * 23)
print('\033[7mCalculadora Automatica de Produção Referencia:\033[1m \033[37;43m941\033[30;m')
print('-=' * 23)

print()
print()
sleep(0.5)

print('\033[1mIndique a linha de produção, 1 ou 2:\033[0m')
print()
sleep(0.3)
linha = int(input('Linha: '))
sleep(0.3)

print()


print('\033[4mPREENCHA COM DADOS DE PRODUÇÃO\033[1m: ')
sleep(0.5)

print()

p = int(input('\033[4mPaletes Completas:\033[0m '))
b = int(input('\033[4mPalete Incompleta:\033[0m '))
df = int(input('\033[4mSucata Fundição:\033[0m '))
dm = int(input('\033[4mSucata Maquinação:\033[0m '))
s = int(input('\033[4mSuspenso:\033[0m '))
if s == None:
    repr(s)

paragem = int(input('Periodo de paragem (min): '))
print()
print()


print('-' * 20)
print('\033[33mA calcular...\033[30m')
print('-' * 20)
sleep(2)
print()

pc = p * 165
tpb = pc + b
tpp = tpb + df + dm + s
ts = df + dm
y = tpp % 8
x = tpp // 8
a = 8 - y
b = y
c = x
d = x + 1
percentparagem = (paragem * 100) / 480
operacional = (100 - percentparagem)

if linha == 1:
    percentagem = (tpp * 100) / 632
if linha == 2:
    percentagem = (tpp * 100) / 432
else:
    print('Linha nao reconhecida. Volte a tentar!')


print('\033[34mProdução Total: {}\n\033[32mProdução Aproveitada: {}\n\033[31mTotal sucata : {}\033[30m'.format(tpp, tpb, ts))

print()
sleep(0.3)

print('{} horas x {} peças\n{} horas x {} peças'.format(a, c, b, d))

print()

print('A calcular percentagens de produção...')
sleep(1)
print()
if percentagem <= 70:
    print('\033[31m{:.2f}\033[30m % Produção'.format(percentagem))
if percentagem >= 70 and percentagem <= 85:
    print('\033[33m{:.2f}\033[30m % Produção'.format(percentagem))
if percentagem >= 85:
    print('\033[32m{:.2f}\033[30m % Produção'.format(percentagem))
print('Operacional: \033[4;35m{:.2f}\033[1;30m % '.format(operacional))
print('RFP: \033[4;35m{:.2f}\033[1;30m %'.format((percentagem * 100) / operacional))

sleep(0.5)
print('-' * 20)
print('-' * 20)

print('\033[37mVersão 0.1.5 alfa\033[30m')
print('Costumer ID: 3640270')
print('Reference No: R1610950')
print('Licença PyCharm Professional ID: UEGWPB5YUC')
print('-' * 10)
bool(input('Prime qualquer tecla para sair'))
exit()
