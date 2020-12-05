vetor = []
for c in range(0, 10):
    n = int(input())
    if n <= 0:
        vetor.append(1)
    else:
        vetor.append(n)
for i in range(0, len(vetor)):
    print(f"X[{i}] = {vetor[i]}")