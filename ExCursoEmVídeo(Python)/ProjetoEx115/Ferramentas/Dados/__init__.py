def leiaInt(x):
    while True:
        try:
            entrada = int(input(x))
        except (ValueError, TypeError):
            print("\033[0;31mErro! Por favor digite um valor inteiro.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[0;34mO usuário encerrou a entrada de dados.\033[m")
            return 3
        else:
            return entrada