s = 0
count = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        count += 1
        s += c
print(f"A soma de todos os {count} números impares, ", end='')
print(f"multiplos de 3 dentro do intervalo de 1-500 é {s}")
