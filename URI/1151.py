n=int(input())
aux=0
anterior=1
x = 1
while x <= n:
    print(aux, end=' ') if x < n else print(aux)
    backup=aux
    aux=aux+anterior
    anterior=backup
    x += 1 