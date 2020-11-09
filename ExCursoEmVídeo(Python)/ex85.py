e = [[], []]
v = 0
for i in range(0, 7):
    v = int(input(f"{i+1}º Valor: "))
    if v % 2 == 0:
        e[0].append(v)
    else:
        e[1].append(v)
print("-=-"*20)
print(f"Os valores impares foram: {sorted(e[1])} ")
print(f"Os valores pares foram: {sorted(e[0])}")
