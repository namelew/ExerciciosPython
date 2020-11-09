n1 = int(input('Digite um valor\n'))
print('-+-'*12)
print(f"Tábuada de {n1}:")
print('-+-'*12)
for c in range(1,11):
    print(f"{n1} * {c} = {n1 * c}")
