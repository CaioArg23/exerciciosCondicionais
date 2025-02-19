#crie uma folha de pagamento mostrando os valores de desconto do IR, FGTS e sindicato
ValorHora = float (input('digite o valor ganho por hora: '))
Hora = float (input('digite quantas horas semanais você trabalha: '))
salarioBruto = ValorHora * (Hora * 3)

if salarioBruto <= 900.00:
    FGTS = salarioBruto * 0.11
    Sindicato = salarioBruto * 0.03
    TotalDescontos = Sindicato
    valorLiquido = salarioBruto - Sindicato
    print (f'valor do salário bruto: {salarioBruto}; \nvalor FGTS: R$:{FGTS}; \nvalor IR (insento): R$:00.00 valor sindicato: {Sindicato}; \ntotal de descontos: {TotalDescontos}; \nvalor liquido salário: {valorLiquido}')

elif salarioBruto > 900.00 and salarioBruto <= 1500.00:
    FGTS = salarioBruto * 0.11
    Sindicato = salarioBruto * 0.03
    IR = salarioBruto * 0.05
    TotalDescontos = Sindicato + IR
    valorLiquido = salarioBruto - TotalDescontos
    print (f'valor do salário bruto: {salarioBruto}; \nvalor FGTS: R$:{FGTS}; \nvalor IR: R$:{IR}; \nvalor sindicato: R$:{Sindicato}; \ntotal de descontos: R$:{TotalDescontos}; \nvalor liquido salário: R$:{valorLiquido}')

elif salarioBruto > 1500.00 and salarioBruto <= 2500.00:
    FGTS = salarioBruto * 0.11
    Sindicato = salarioBruto * 0.03
    IR = salarioBruto * 0.10
    TotalDescontos = Sindicato + IR
    valorLiquido = salarioBruto - TotalDescontos
    print (f'valor do salário bruto: {salarioBruto}; \nvalor FGTS: R$:{FGTS}; \nvalor IR: R$:{IR}; \nvalor sindicato: R$:{Sindicato}; \ntotal de descontos: R$:{TotalDescontos}; \nvalor liquido salário: R$:{valorLiquido}')

elif salarioBruto > 2500.00:
    FGTS = salarioBruto * 0.11
    Sindicato = salarioBruto * 0.03
    IR = salarioBruto * 0.20
    TotalDescontos = Sindicato + IR
    valorLiquido = salarioBruto - TotalDescontos
    print (f'valor do salário bruto: {salarioBruto}; \nvalor FGTS: R$:{FGTS}; \nvalor IR: R$:{IR}; \nvalor sindicato: R$:{Sindicato}; \ntotal de descontos: R$:{TotalDescontos}; \nvalor liquido salário: R$:{valorLiquido}')