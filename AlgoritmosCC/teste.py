tempo = input().split()
s = int(tempo[0])
t = int(tempo[1])
f = int(tempo[2])
if s + t + f <= 23:
    print(s + t + f)
else:
    print((s + t + f) - 24)
