#faça um programa que peça 3 lados de um triângulo. O programa deverá informar se os valores podem ser um trangulo
#escaleno, isosceles ou quilatero

L1 = float(input('digite um lado do triângulo: '))
L2 = float(input('digite mais um lado do triângulo: '))
L3 = float(input('digite outro lado do triângulo: '))

if L1 == L2 and L1 == L3:
    print ('o triângulo é equilátero')

elif L1 == L2 or L1 == L3 or L2 == L3:
    print('o triangulo é isósceles')

elif L1 != L2 and L1 != L3:
    print('o triângulo é escaleno')