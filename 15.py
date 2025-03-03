dia = int(input('digite o dia: '))
mes = int(input('digite o número do mês: '))
ano = int(input('digite o ano: '))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia > 31:
        print('digite um dia menor ou igual a 31')

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 30:
        print('digite um dia menor ou igual a 30')

elif mes == 2:
    if dia > 28:
        print('digite um dia menor ou igual a 28')


print(f'{dia}/{mes}/{ano}')