def soma(*num):
    s = 0
    for n in num:
        s += n
    print(f"A soma dos valores {num} é {s}")
    print()
def cont(*x):
    #for v in x:
    #    print(f"{v} ", end='')
    #print('Fim!')
    print(f"Recebi os valores {x} e ao todo são {len(x)} números")
def dobra(v):
    pos = 0
    while pos < len(v):
        v[pos] *= 2
        pos += 1
    print(v)



#programa principal
soma(4, 5)
#soma(b=4, a=5)
soma(8, 9)
#soma(2, 1)
cont(3, 2, 5)
#cont(2, 6)
#cont(6, 7, 8, 9, 2)
#v = [7, 2, 5, 0, 4]
#dobra(v)