cesar = []
orig = []
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = int(input())
for i in range(0, c):
    cifra = input()
    n = int(input())
    ent = [cifra, n]
    cesar.append(ent.copy())
    ent.clear()
reversed(cesar)
for p in cesar:
    for a in p[0]:
        pos = alfabeto.index(a)
        andar = pos - p[1]
        orig.append(alfabeto[andar])
    print(''.join(orig))
    orig.clear()