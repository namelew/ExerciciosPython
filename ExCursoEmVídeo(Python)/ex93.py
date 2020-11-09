from time import sleep as sp
gols = []
s = 0
jogador = {
    'nome': input("Nome Jogador: ").capitalize(),
    'partidas': gols,
}
q = int(input(f"Quantas partidas {jogador['nome']} jogou?\n"))
for i in range(0, q):
    gols.append(int(input(f"Quantos gols na {i+1}ª partida? ")))
    s += gols[i]
jogador['total'] = s
print("-="*20)
print(jogador)
print("-="*20)
for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}.")
    sp(1)
print("-="*20)
print(f"O jogador {jogador['nome']} jogou {q} partidas.")
for i, v in enumerate(gols):
    print(f"    => Na partida {i+1}, fez {v} gols.")
    sp(1)
print(f"Foi um total de {s} gols.")
