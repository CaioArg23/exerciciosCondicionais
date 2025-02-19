#faça um programa que peça dois valores e guarde um duas variáveis, depois inverta os dois valores das variáveis
n1 = int(input('escreva um primeiro número inteiro: ')) 
n2 = int(input('escreva um segundo número inteiro: '))
n3 = n1

if n1 > n2:
    n1 = n2
    print (f'o primeiro número agora vale: {n1}')
    
    if n1 == n2:
        print (f'o segundo número agora vale: {n3}')

elif n1 < n2:
    n1 = n2
    print (f'o primeiro número agora é {n1}')

    if n1 == n2:
        print (f"agora o segundo número é o {n3}")    