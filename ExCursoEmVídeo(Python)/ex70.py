print("=" * 30)
print(f"{'VAREJÃO DO PAULÃO':^30}")
print("=" * 30)
nb = ""
g = comp = vm = 0
i = 1
while True:
    p = str(input("Nome do Produto: "))
    v = float(input("Preço do Produto: R$ "))
    c = str(input("Deseja adicionar mais produtos?[S/N]: ")).upper().strip()[0]
    while c not in "SN":
        c = str(input("Deseja adicionar mais produtos?[S/N]: ")).upper().strip()[0]
    g += v
    if i == 1 or v < comp:
        nb = p
        comp = v
    if v > 1000:
        vm += 1
    if c in "Nn":
        break
    i += 1
print(f"{' FIM DO PROGRAMA ':-^40}")
print(f"Gasto Total = R$ {g:.2f}\nProduto Mais Barato = {nb.capitalize()} (R$ {comp:.2f})")
print(f"Q. Produtos Que Custaram mais de R$ 1000 = {vm}")
