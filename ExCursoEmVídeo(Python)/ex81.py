l = []
while True:
    n = int(input("Digite um valor: "))
    l.append(n)
    r = " "
    while r not in "SsNn":
        r = str(input("Deseja continuar? [S/N] ")).strip()[0]
    if r in "Nn":
        break
print(f"Foram digitados {len(l)} números;\nOs números em ordem decrescentes são {sorted(l, reverse=True)};")
if 5 in l:
    print("E o número 5 está dentro da lista.")
else:
    print("E o número 5 não está na lista.")
