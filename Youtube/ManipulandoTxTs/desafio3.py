with open('inscritos.txt', 'r') as arq:
    c = 1
    for v in arq:
        print(f"{c}-{v}")
        c += 1
