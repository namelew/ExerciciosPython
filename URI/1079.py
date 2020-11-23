n=int(input())
c = 1
while c <= n:
    n1, n2, n3 = map(float, input().split())
    print("%.1f"%(((n1*2)+(n2*3)+(n3*5))/10))
    c += 1