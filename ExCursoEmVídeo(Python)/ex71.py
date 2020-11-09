print("=" * 30)
print(f"{'BANCO MONÉRA':^30}")
print("=" * 30)
valor = int(input("Saque: R$ "))
total = valor
c = 0
ced = [100, 50, 20, 10, 5, 2, 1]
while True:
    if valor >= ced[c]:
        nota = valor // ced[c]
        print(f"Total de {nota} notas de R$ {ced[c]}")
        valor = valor % ced[c]
    c += 1
    if valor == 0:
        break
print("=" * 30)
print("Volte sempre e tenha um bom dia!")
