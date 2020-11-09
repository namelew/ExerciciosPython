n = int(input("Insira um número: "))
f = 0
for c in range(1, n+1):
    if n % c == 0 and c == n or c == 1:
        f += 1
if f == 2:
    print("Este número é primo")
elif f > 2:
    print("Este número não é primo")
