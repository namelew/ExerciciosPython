l = []
pares = []
impares = []
while True:
    n = int(input("Digite um valor: "))
    l.append(n)
    r = "1"
    while r not in "SsNn":
        r = str(input("Deseja continuar? [S/N] ")).strip()[0]
    if r in "Nn":
        break
for c in range(0, len(l)):
    if l[c] % 2 == 0:
        pares.append(l[c])
    else:
        impares.append(l[c])
print(f"Os valores digitados foram {l};\nDentre eles {pares} são valores pares;")
print(f"E {impares} são valores impares.")
