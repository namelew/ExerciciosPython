def voto(ano):
    """
    -> Recebe a data de nascimento de uma pessoa e retorna se ela pode ou não votar
    :param ano: ano de nascimento
    :var x: idade da pessoa
    :return: x e se o voto dela é OBRIGATÓRIO, NEGADO ou OPCIONAL
    """
    from datetime import date
    x = date.today().year - ano
    if 18 <= x <= 70:
        return print(f"Com idade {x}, voto: OBRIGATÓRIO.")
    elif x < 16:
        return print(f"Com idade {x}, voto: NEGADO.")
    else:
        return print(f"Com idade {x}, voto: OPCIONAL.")


print("-" * 30)
an = int(input("Em que ano você nasceu? "))
print("-=" * 20)
voto(an)
print("-=" * 20)
