m = [[], [], []]
s = st = mv = 0
for l in range(0, 3):
    for c in range(0, 3):
        m[l].append(int(input(f"Espaço ({l}, {c}): ")))
        if m[l][c] % 2 == 0:
            s += m[l][c]
        if c == 2:
            st += m[l][c]
        if l == 1 and c == 0:
            mv = m[l][c]
        elif l == 1 and c != 0:
            if m[l][c] > mv:
                mv = m[l][c]
print("-="*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{m[l][c]:^5}]", end=' ')
    print()
print("-="*30)
print(f"A soma dos elementos pares é {s};\nA somatória de todos os elementos da 3ª coluna é {st};")
print(f"E o maior valor da 2ª linha é {mv}.")
