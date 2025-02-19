#faça  um programa que calcule raízes de uma equação do segundo grau, na forma ax²+ bx + c
#o programa deverá pedir os valores A, B e C e fazer as consistências, informando ao usuário as seguintes situações:

import math

ax = float(input("Digite o valor de a: "))
bx = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))


delta = bx**2 - (4 * ax * c)

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    
    raiz_delta = math.sqrt(delta)
    x1 = (-bx + raiz_delta) / (2 * ax)
    x2 = (-bx - raiz_delta) / (2 * ax)

    print(f"As raízes da equação são: x1 = {x1:.2f} e x2 = {x2:.2f}")
