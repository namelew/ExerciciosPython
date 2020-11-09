print("Digite 999 para sair:")
n = int(input("Digite um número: "))
s = c = 0
while n != 999:
    s += n
    c += 1
    n = int(input("Digite um número: "))
print(f"A soma dos {c} números inteiros digitados é {s}")
