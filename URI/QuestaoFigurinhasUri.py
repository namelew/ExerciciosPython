casos = []
c = int(input())
for i in range(0, c):
    a, b = map(int, input().split())
    ent = [a, b]
    casos.append(ent.copy())
    ent.clear()
for ca in casos:
    mdc = ca[0]
    while ca[0] % mdc != 0 or ca[1] % mdc != 0:
        mdc = mdc - 1
    print(mdc)
