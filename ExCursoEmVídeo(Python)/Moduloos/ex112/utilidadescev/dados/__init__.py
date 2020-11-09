def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f"\033[0;31mErro! \"{entrada}\" é um preço inválido.\033[m")
        else:
            v = True
            return float(entrada)


def leiaInt(x):
    ok = False
    v = 0
    while True:
        n = str(input(x))
        if n.isnumeric():
            v = int(n)
            ok = True
        else:
            print(f"\033[0;31mErro! {n} não é um valor válido.\033[m")
        if ok:
            break
    return v
