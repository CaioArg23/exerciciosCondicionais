#escreva um programa que analise notas de alunos seguindo a seguinte tabela
#entre 10 e 9 A
#entre 9 e 7.5 B
#entre 7.5 e 6 C
#entre 6 e 4 D
#entre 4 e 0 E
# A,B,C = APROVADO e D,E = REPROVADO

nota = float(input('digite a nota do seu aluno: '))

if nota <=10 and nota >=9:
    print ('NOTA A: APROVADO')

elif nota < 9 and nota >=7.5:
    print('NOTA B: APROVADO')

elif nota < 7.5 and nota >=6:
    print('NOTA C: APROVADO')

elif nota < 6 and nota >=4:
    print ('NOTA D: REPROVADO')

elif nota < 4 and nota >=0:
    print('nota E: REPROVADO')

else: 
    print('digite um número correspondente')