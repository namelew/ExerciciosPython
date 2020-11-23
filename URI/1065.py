pares = 0
c = 1
while c <= 5:
    n = int(input())
    if n % 2 == 0:
        pares += 1
    c += 1
print(pares,"valores pares")