entrada = []
proc = []
c = 0
pma = pm = 0
while True:
    entrada.append(str(input("Nome: ")))
    entrada.append(float(input("Peso(Kg): ")))
    if len(proc) == 0:
        pma = pm = entrada[1]
    else:
        if entrada[1] > pma:
            pma = entrada[1]
        if entrada[1] < pm:
            pm = entrada[1]
    c += 1
    proc.append(entrada[:])
    entrada.clear()
    r = str(input("Deseja continuar?[S/N] ")).strip()[0]
    while r not in "NnSs":
        print("Opção inválida! Digite novamente!")
        r = str(input("Deseja continuar?[S/N] ")).strip()[0]
    if r in "Nn":
        break
print("-=-"*15)
print(f"{'DADOS':^45}")
print("-=-"*15)
print(f"Número de Pessoas: {c}")
print(f"O maior peso foi {pma:.2f} Kg. E as pessoas mais pesadas foram: ", end="")
for p in proc:
    if p[1] == pma:
        print(p[0], end=' ')
print(".")
print(f"O menor peso foi {pm:.2f} Kg. E as pessoas mais leves foram: ", end="")
for p in proc:
    if p[1] == pm:
        print(p[0], end=' ')
print(".")
