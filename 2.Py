#faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:

#a mensagem "aprovado", se a média alcançada for maior ou igual a sete
#a mensagem "reprovado", se a média for menor que sete
#a mensagem "aprovado com Distinção", se a média for igual a dez

nota1 = int(input('digite a primeira nota do aluno: '))
nota2 = int(input('digite a segunda nota do aluno: ')) 
media = (nota1 + nota2)/2

if media == 10:
    print ('aprovado com distinção')

elif media >= 7:
    print ('aprovado')

elif media < 7: 
    print ('reprovado')

else:
    print ('valor muito alto')