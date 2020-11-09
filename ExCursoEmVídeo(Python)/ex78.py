l = []
for c in range(0, 5):
    a = int(input(f"Posição {c}: "))
    l.append(a)
print(f"Os valores digitados foram {l}")
print(f"O maior valor foi {max(l)} e apareceu nas posições ", end='')
for p, v in enumerate(l):
    if max(l) == v:
        print(p, end=' ')
print(f"\nO menor valor foi {min(l)} e apareceu nas posições ", end='')
for p, v in enumerate(l):
    if min(l) == v:
        print(p, end=' ')
