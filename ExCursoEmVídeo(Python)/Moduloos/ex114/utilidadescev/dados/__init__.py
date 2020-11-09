def leiaDinheiro(msg):
    while True:
        try:
            entrada = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print("\033[0;31mErro! Digite um valor válido!\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[0;34mO usuário interrompeu a entrada de dados.\033[m")
            return 0.0
        else:
            return entrada


def leiaInt(x):
    while True:
        try:
            n = int(input(x))
        except KeyboardInterrupt:
            print("\n\033[0;34m;mEntrada de dados interrompida pelo usuário.\033[m")
            return -1
        except (ValueError, TypeError):
            print('\033[0;31mErro! Por favor digite um número inteiro válido.\033[m')
            continue #joga para o início do laço
        else:
            return n


def leiaFloat(x):
    while True:
        try:
            entrada = float(input(x).replace(',', '.'))
        except KeyboardInterrupt:
            print("\n\033[0;34mEntrada de dados interrompida pelo usuário.\033[m")
            return 0.0
        except (TypeError, ValueError):
            print("\033[0;31mErro! Digite um valor decimal válido.\033[m")
            continue
        else:
            return entrada


def acessaSites(x):
    """
    -> Testa se uma url pode ser acessada
    :param x: url
    :return: none
    """
    import urllib.request
    try:
        site = urllib.request.urlopen(x)
    except:
        print("\033[0;31mO site não pode ser acessado.\033[m")
    else:
        print("\033[0;34mO site pode ser acessado.\033[m")
        site.read() #retorna conteúdo html do site
