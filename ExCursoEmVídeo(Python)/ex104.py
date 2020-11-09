def leiaInt(x):
    ok = False
    v = 0
    while True:
        n = str(input(x))
        if n.isnumeric():
            v =int(n)
            ok = True
        else:
            print(f"\033[0;31mErro! {n} não é um valor válido.\033[m")
        if ok:
            break
    return v


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar {n}.")
