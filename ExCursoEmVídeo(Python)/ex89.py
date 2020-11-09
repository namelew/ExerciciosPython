entrada = []
alunos = []
media = []
while True:
    entrada.append(input("Nome: "))
    entrada.append(float(input("Nota 1ª: ")))
    entrada.append(float(input("Nota 2ª: ")))
    s = entrada[1] + entrada[2]
    media.append(s/2)
    alunos.append(entrada[:])
    entrada.clear()
    o = input("Deseja continuar[S/N]: ")
    while o not in "SsNn":
        o = input("Deseja continuar[S/N]: ")
    if o in "Nn":
        break
print("-="*30)
print(f"{'No.':<4}", f"{'Nome':<10}", f"{'Média':>8}")
for i in range(0, len(alunos)):
    print(f"{i:<4}", f"{alunos[i][0]:<10}", f"{media[i]:>8.1f}")
print("-="*30)
while True:
    c = int(input("Digite o Número do Aluno para ver detalhes da sua nota(Digite 999, para sair): "))
    if c == 999:
        break
    print(f"Notas Aluno(a) {alunos[c]}:\nNota 1: {alunos[c][1]:.1f}\nNota 2: {alunos[c][2]:.1f}")
