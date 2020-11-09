n = int(input("Digite um número: "))
s = m = i = p = 0
while n != 0:
    if n % 2 == 0:
        p += 1
    else:
       i += 1
    m += 1
    s += n
    n = int(input("Digite um número: "))
print(f"Média dos Números: {s/m:.2f}")
print("Pares:", p)
print("Inpares:", i)
