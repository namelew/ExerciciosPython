array = []
n = int(input())
entrada = input().split()
for i in entrada:
    array.append(int(i))
minimo = min(array)
pos = array.index(minimo)
print(f"Menor valor: {minimo}\nPosicao: {pos}")