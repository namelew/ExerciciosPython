from random import shuffle
n1 = input('Aluno 1\n')
n2 = input('Aluno 2\n')
n3 = input('Aluno 3\n')
n4 = input('Aluno 4\n')
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('-'*20)
print('Ordem de Apresentação')
print(f'A ordem de apresentação será: {alunos}')
print('-'*20)
