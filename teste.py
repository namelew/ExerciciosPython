def nperfeito(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
    if sum(div) == n:
        return 1
    return 0

n = int(input())
if nperfeito(n) == 1:
    print(f"{n} é um número inteiro positivo perfeito")
else:
    print(f"{n} não é um número inteiro positivo perfeito")