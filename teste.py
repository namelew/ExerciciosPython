pares = []
impares = []
entrada = input().split()
for item in entrada:
    if int(item) % 2 == 0:
        pares.append(int(item))
    else:
        impares.append(int(item))
print("Pares: ", end='')
for n in pares:
    print(n, end=' ')
print()
print("Impares: ", end='')
for n in impares:
    print(n, end=' ')
print()