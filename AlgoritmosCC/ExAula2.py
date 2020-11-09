v = []
print("Para finalizar digite -1")
while True:
    n = int(input("Digite um valor: "))
    if n == -1:
        break
    v.append(n)
i = (len(v)-1)//2
print("Valor Central = {}".format(v[i]))