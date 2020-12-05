vetor = []

for i in range(0, 100):
    n = float(input())
    vetor.append(n)

for it in range(0, len(vetor)):
    if vetor[it] <= 10:
        print(f"A[{it}] = {vetor[it]}")