x=int(input())
c = 1
while c <= x:
    temp = 2
    ehprimo = True
    n=int(input())
    while temp <= n:
        if(n % temp == 0 and temp != n):
            ehprimo = False
            break
        temp += 1
    if ehprimo:
        print(n, "eh primo")
    else:
        print(n, "nao eh primo")
    c += 1