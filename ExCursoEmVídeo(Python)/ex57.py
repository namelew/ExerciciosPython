s = str(input("Sexo[M/F]: ")).upper().strip()[0]
while s not in "MmFf":
    print("\033[1;31mDigite uma opção válida!\033[m")
    s = input("Sexo[M/F]: ").upper().strip()[0]
if s == "M":
    print("Sexo masculino adicionado com sucesso!")
else:
    print("Sexo feminino adicionado com sucesso!")
