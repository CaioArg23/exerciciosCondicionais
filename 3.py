#faça um programa que peça três número e exiba o maior entre eles
n1 = int(input('digite um número inteiro: '))
n2 = int(input('digite mais um número inteiro: '))
n3 = int (input('digite outro número inteiro: '))

if n1 > n2 and n1 > n3:
    print (f'o maior número é {n1}')

elif n2 > n1 and n2 > n3:
    print (f'o maior número é {n2}')

elif n3 > n1 and n3> n2:
    print (f'o maior número é {n3}')