numeros = []
entrada = input().split()
for i in entrada:
    numeros.append(int(i))
for n in sorted(numeros):
    print(n)
print()
for it in numeros:
    print(it)