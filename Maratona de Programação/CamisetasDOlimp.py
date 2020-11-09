pedidos = [[], [], []]
n = int(input())
t = input()
pedidos[0].append(t.split(' '))
for c in pedidos[0]:
    if c == "1":
        pedidos[1].append(c)
    if c == '2':
        pedidos[2].append(c)
fp = int(input())
fm = int(input())
if fp >= len(pedidos[0]) and fm >= len(pedidos[1]):
    print("S")
else:
    print("N")
