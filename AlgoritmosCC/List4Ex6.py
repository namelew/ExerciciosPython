n = int(input("Número: "))
f = n
fa = 1
print(f"{n}! = ", end= '')
while f > 0:
    print(f"{f}", end='')
    print(" x " if f > 1 else " = ", end='')
    fa *= f
    f -= 1
print(f"{fa}")
