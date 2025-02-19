#faça um programa que pergunte em que turno você estuda
#M - matituno (bom dia)
#V -  vespertino (boa tarde)
#N - noturno (boa noite)
#valor invalido

print ('M (matituno) V (vespertino) N (noturno)' )
turno = str(input('digite o turno que você estuda: '))

if turno == 'M':
    print ('você estuda no período matituno')

elif turno == 'V':
    print ('você estuda no período vespertino')

elif turno == 'N':
    print ('você estuda no período noturno')

else:
    print ('escreva uma letra disponível')