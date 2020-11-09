def aumentar(x=0, a=0):
    return x + (x * a / 100)


def diminuir(x=0, d=0):
    return x - (x * d / 100)


def dobro(x=0):
    return x * 2


def metade(x=0):
    return x / 2


def moeda(p=0, m='R$'):
    return f'{m} {p:.2f}'.replace('.', ',')
