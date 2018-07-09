from time import sleep

print()
sleep(0.5)
print('Calculadora Automatica de Produção\nReferencia 941')
print()
print()
sleep(0.5)
print('Insira valores de produção:')
sleep(0.5)
p = int(input('Paletes Completas: '))
b = int(input('Palete Incompleta: '))
df = int(input('Sucata Fundição: '))
dm = int(input('Sucata Maquinação: '))
s = int(input('Suspenso: '))


print('-' * 20)
print('\033[33mA calcular...\033[30m')
print('-' * 20)
sleep(2)


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
percentagem = (tpp * 100) / 632

print('\033[34mProdução Total: {}\n\033[32mProdução Aproveitada: {}\n\033[31mTotal sucata : {}\033[30m'.format(tpp, tpb, ts))
print()
print('{} horas x {} peças\n{} horas x {} peças'.format(a, c, b, d))
print()
if percentagem <= 70:
    print('\033[31m{:.2f}\033[30m % Produção'.format(percentagem))
if percentagem >= 70 and percentagem <= 85:
    print('\033[33m{:.2f}\033[30m % Produção'.format(percentagem))
if percentagem >= 85:
    print('\033[32m{:.2f}\033[30m % Produção'.format(percentagem))
print('-' * 20)


print('-' * 20)
print('Versão 0.01 alfa')
print('Costumer ID: 3640270')
print('Reference No: R1610950')
print('Licença PyCharm Professional ID: UEGWPB5YUC')
print('-' * 20)
bool(input('Prime qualquer tecla para sair'))
exit()


