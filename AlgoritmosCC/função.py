# def cpf():
#  nome = input("Nome: )
#  cpf = int(input("CPF: "))
#  print(nome)
#  print(cpf)
#  return()
# cpf()
alunos = [[], [], []]
s = 0


def media(x, y):
    media = x / y
    return media


for i in range(2):
    no = input("Nome: ")
    alunos[0].append(no)
    for n in range(2):
        n1 = float(input(f"Nota {n + 1}: "))
        alunos[1].append(n1)
        s += n1
    alunos[2].append(media(s, n + 1))
    alunos[1].clear()
    s = 0
print("=+"*20)
for i in range(len(alunos[0])):
    print(f"Aluno: {alunos[0][i]}\nMédia: {alunos[2][i]:.2f}")
