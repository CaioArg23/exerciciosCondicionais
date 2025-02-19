#Faça um programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ['a', 'e', 'i', 'o', 'u'] #criando variável das vogais com uma lista
pergunta = input('digite uma letra em minúsculo: ')

if pergunta in vogais:
    print (f'a letra que você digitou "{pergunta}" é vogal') 

else:
    print (f'a letra que você digitou "{ pergunta}" é consoante')