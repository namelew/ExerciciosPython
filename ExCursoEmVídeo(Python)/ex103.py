def ficha(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


n = str(input("Nome Jogador: "))
ng = str(input("N. Gols: "))
if ng.isnumeric():
    ng = int(ng)
else:
    ng = 0
if n.strip() == '':
    ficha(gols=ng)
else:
    ficha(n, ng)

