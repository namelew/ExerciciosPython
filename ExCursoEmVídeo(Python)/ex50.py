print("Somatória dos números: ")
s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f"Digite o {c} valor: "))
    if n % 2 == 0:
        cont += 1
        s += n
print(f"A somatória dos {cont} números pares foi {s}")
