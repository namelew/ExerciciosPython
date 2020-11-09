cor = (
    '\033[m',  # 0 - sem cor
    '\033[1;30m',  # 1 - branco
    '\033[1;31m',  # 2 - vermelho
    '\033[1;32m',  # 3 - verde
    '\033[1;33m',  # 4 - amarelo
    '\033[1;34m',  # 5 - azul
    '\033[1;35m',  # 6 - roxo
    '\033[1;36m',  # 7 - magenta
    '\033[1;37m'  # 8 - cinza
)


def titulo(msg, c=0, tan=0):
    if tan == 0:
        tam = len(msg) + 4
    else:
        tam = tan
    print(f"{cor[c]}-"*tam)
    print(f"{msg}".center(tam))
    print(f"-{cor[c]}" * tam, end='')
    print(cor[0])


def linha(tam=42):
    return "-" * tam

