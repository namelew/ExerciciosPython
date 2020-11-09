from random import choice
nome1 = input('Digite o nome do primeiro aluno ')
nome2 = input('Digite o nome do segundo aluno ')
nome3 = input('Digite o nome do terceiro aluno ')
nome4 = input('Digite o nome do último aluno ')
lista = [nome1, nome2, nome3, nome4]
print(f'O sorteado foi {choice(lista)}')
