m = [[], [], []]
print("Gerador de Matriz 3x3")
for i in range(0, 3):
    m[0].append(int(input(f"Valor Linha 1: ")))
    m[1].append(int(input(f"Valor Linha 2: ")))
    m[2].append(int(input(f"Valor Linha 3: ")))
#Outra forma:
#for l in range(0, 3):
#   for c in range(0, 3):
#       m[l].append(int(input("Valor Posição ({}, {}): ".format(l, c))))
print("-=-"*20)
print("{}\n{}\n{}".format(m[0], m[1], m[2]))
#Outra forma:
#for l in range(0, 3):
#   for c in range(0, 3):
#       print(f"[{m[l][c]:^5}]")
#   print()
