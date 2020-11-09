v = []
a = 0
for i in range(10):
    a = int(input())
    v.append(a)
for n in range(len(v)-1, -1, -1):
    print(v[n])