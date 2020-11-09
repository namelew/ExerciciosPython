from random import randint
from time import sleep as sp
def sorteia(list):
    n = randint(0, 10)
    while len(list) < 5:
        if n not in list:
            list.append(n)
        else:
            n = randint(0, 10)
    print("Os valores sorteados foram ", end='')
    for v in list:
        print(v, end=' ', flush=False)
        sp(1)
    sp(1)
    print("PRONTO!")
def somaPar(list):
    s = 0
    for i in list:
        if i % 2 == 0 and i != 0:
            s += i
    print(f"A soma dos valores pares da lista é {s}.")


lista = []
sorteia(lista)
somaPar(lista)