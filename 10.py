#faça um programa que leia um número e exiba o dia correspondente da semana (1- domingo), (2-segunda e etc...)
diaSemana = str(input('digite um número correspondente aos dias da semana: '))

if diaSemana == "1":
    print ('hoje é domingo')

elif diaSemana == "2":
    print ('hoje é segunda-feira')

elif diaSemana == "3":
    print ('hoje é terça-feira') 

elif diaSemana == "4":
    print ('hoje é quarta-feira')

elif diaSemana == "5":
    print ('hoje é quinta-feira')

elif diaSemana == "6":
    print ('hoje é sexta-feira')

elif diaSemana == "7":
    print ('hoje é sábado')

else:
    print ('digite um número correspondente')