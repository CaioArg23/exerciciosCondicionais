#faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério baseado no salario atual:
#salarios até R$ 280,00 (incluindo): aumento de 20%
#salários de até R$ 280,00 e R$ 700,00: aumento de 15%
#salários de até R$ 700,00 e R$1500,00: aumento de 10%
#salários de até R$ 1500 diante: aumento de 5% após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual do aumento aplicado

salario =  float(input('digite o seu salário para saber o valor do seu aumento: '))
salario1 = salario

if salario <=280.00:
    percentual = salario * 0.20 
    valorFinal = salario + percentual
    print (f'o valor do seu salário era: {salario1}, você ganhou 20% de aumento e ficou: {valorFinal}')

elif salario > 280.00 and salario < 700.00:
    percentual = salario * 0.15 
    valorFinal = salario + percentual
    print (f'o valor do seu salário era: {salario1}, você ganhou 15% de aumento e ficou: {valorFinal}')

elif salario > 700.00 and salario < 1500.00:
    percentual = salario * 0.10
    valorFinal = salario + percentual
    print (f'o valor do seu salário era: {salario1}, você ganhou 10% de aumento e ficou: {valorFinal}')

elif salario > 1500.00:
    percentual = salario * 0.05
    valorFinal = salario + percentual
    print (f'o valor do seu salário era: {salario1}, você ganhou 5% de aumento e ficou: {valorFinal}')

else:
    print ('escreva um número válido')