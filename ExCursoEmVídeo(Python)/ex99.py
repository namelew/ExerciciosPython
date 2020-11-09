def maior(*x):
    m = 0
    if len(x) <= 0:
        print("Não foram informados valores.")
    else:
        for v in range(0, len(x)):
            if x[v] > m or v == 0:
                m = x[v]
        print(f"Foram digitados {len(x)} valores e ", end='')
        print(f"o maior valor dentre eles {x} é {m}")


maior(1, 3, 4, 5, 6, 7, 8, 99, 91)
maior()
