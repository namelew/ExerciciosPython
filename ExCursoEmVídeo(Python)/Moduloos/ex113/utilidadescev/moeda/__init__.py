def aumentar(x=0, a=0, f=False):
    """
    -> Aumenta o preço de x pelo percentual a
    :param x: Valor a ser aumentado
    :param a: Percentual de Aumento
    :param f: (Opcional)Formatação da Moeda(Ex: 500.0 -> R$ 500,00)
    :return: Valor aumentado pelo percentual a.
    """
    res = x + (x * a / 100)
    return res if f is False else moeda(res)


def diminuir(x=0, d=0, f=False):
    """
    -> Diminui x pelo percentual d
    :param x: Valor a ser diminuido
    :param d: Percentual de Diminuição
    :param f: (Opcional)Formatação da Moeda(Ex: 500.0 -> R$ 500,00)
    :return: retorna o valor reduzido por d
    """
    res = x - (x * d / 100)
    return res if f is False else moeda(res)


def dobro(x=0, f=False):
    """
    -> Dobra o valor de x
    :param x: valor a ser dobrado
    :param f: (Opcional)Formatação da Moeda(Ex: 500.0 -> R$ 500,00)
    :return: retorna o valor dobrado
    """
    res = x * 2
    return res if not f else moeda(res)


def metade(x=0, f=False):
    """
    -> Dividi pela metade o valor de x
    :param x: valor a ser dividido
    :param f: (Opcional)Formatação da Moeda(Ex: 500.0 -> R$ 500,00)
    :return: retorna o valor dividido
    """
    res = x/2
    return res if f is False else moeda(res)


def moeda(p=0, m='R$'):
    """
    -> Converte o valor de p para uma formatação de moeda
    :param p: valor a ser formatado
    :param m: moeda a ser utilizada
    :return: retorna o valor formatado
    """
    return f'{m} {p:.2f}'.replace('.', ',')


def resumo(p, a=0, d=0):
    """
    -> Gera uma tabela de resumo das outras funções do módulo
    :param p: Valor a ser analizado
    :param a: (Opcional)Percentual de aumento
    :param d: (Opcional)Percentual de diminuição
    :return: none
    """
    print('-' * 30)
    print(f'RESUMO VALOR'.center(30))
    print('-' * 30)
    print(f"Valor analizado: \t{moeda(p)}")
    print(f"Dobro: \t\t\t\t{dobro(p, True)}")
    print(f"Metade: \t\t\t{metade(p, True)}")
    print(f"Aumento de {a} %: \t{aumentar(p, a,  True)}")
    print(f"Diminuição de {d} %:\t{diminuir(p, d, True)}")
    print('-' * 30)
