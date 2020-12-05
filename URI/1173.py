vetor = []
v = int(input())
for i in range(0, 10):
    vetor.append(v)
    v *= 2
for i in range(0, len(vetor)):
    print(f"N[{i}] = {vetor[i]}")