import random
A1 = str(input('Digite o nome do aluno: '))
A2 = str(input('Digite o nome do aluno: '))
A3 = str(input('Digite o nome do aluno: '))
A4 = str(input('Digite o nome do aluno: '))
Alunos = [A1, A2, A3, A4]
ordem = random.shuffle(Alunos)
print('A ordem de apresentação é: {} '.format(Alunos))
