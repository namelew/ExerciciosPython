c = s = 0
while True:
    n = int(input("Digite um número inteiro(999 para): "))
    if n == 999:
        break
    s += n
    c += 1
print(f"A soma dos {c} valores foi {s}")
