#faça um programa que leia três números e mostre-os em ordem decrescente
n1 = int(input('escreva um número: '))     
n2 = int(input('escreva mais um número: '))
n3 = int(input('escreva outro número: '))  
#não vou utilizar condicionais e sim listas pois é mais pratico

decrescente = [n1, n2, n3]
decrescente.sort(reverse=True)

print (decrescente)