from random import randint as rd
from time import sleep
lista = []
jogos = []
print("-" * 30)
print(f"{'Sortando Jogos na Mega Sena':^30}")
print("-" * 30)
q = int(input("Quantos jogos devo sortear? "))
t = 1
while t <= q:
    c = 0
    while True:
        n = rd(1, 60)
        if n not in lista:
            lista.append(n)
            c += 1
        if c >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    t += 1
print("-=" * 3, f"Sorteando {q} Jogos", "-=" * 3)
sleep(0.5)
for i, o in enumerate(jogos):
    print(f"Jogo {i+1}: {o}")
    sleep(1)
print("-=" * 3, "BOA SORTE", "-=" * 3)