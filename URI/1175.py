vetor = []
for i in range(20):
    n=int(input())
    vetor.append(n)
reverso = vetor[::-1]
for j in range(20):
    print(f'N[{j}] = {reverso[j]}')