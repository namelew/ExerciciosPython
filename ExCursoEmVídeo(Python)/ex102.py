def fatorial(n, show=False):
    """
    -> Recebe um número e mostra o fatorial dele. Também pode ou não mostrar o cálculo.
    :param n: número o qual será mostrado o fatorial
    :param show:(opcional) Mostrar ou não o cálculo desse fatorial
    :return: retorna o valor do fatorial
    """
    f = 1
    print(f"{n}! = ", end='')
    for v in range(n, 0, -1):
        if show:
            print(f"{v} x " if v > 1 else f"{v} = ", end='')
        f *= v
    return f


#Programa Principal
print(fatorial(5, show=True))
