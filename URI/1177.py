array = []
clone = []
x = int(input())
terminou = False
for i in range(x):
    array.append(i)
for n in range(1000):
    if terminou:
        break
    for it in array:
        clone.append(it)
        if len(clone) >= 1000:
            terminou = True
            break
for c in range(len(clone)):
    print(f"N[{c}] = {clone[c]}")