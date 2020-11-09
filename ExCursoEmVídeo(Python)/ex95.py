partidas = []
time = []
jogador = {}
while True:
    s = 0
    jogador['nome'] = input("Nome do Jogador: ").capitalize()
    q = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for i in range(0, q):
        partidas.append(int(input(f"    Quantos gols na {i + 1}ª partida? ")))
        s += partidas[i]
    jogador['partidas'] = partidas[:]
    jogador['total'] = s
    time.append(jogador.copy())
    partidas.clear()
    while True:
        c = input("Deseja continuar[S/N]? ")[0].upper()
        if c in "SN":
            break
        print("Erro! Digite S ou N.")
    if c in "N":
        break
print("-=" * 30)
print("cod ", end='')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()
print("-"*40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("-" * 40)
while True:
    c = int(input("Mostrar os dados de qual jogador?(999 para parar) "))
    if c == 999:
        break
    if c >= len(time):
        print("Erro! Código inválido, não existe jogador com esse código.")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[c]['nome']}:")
        for i, g in enumerate(time[c]['partidas']):
            print(f"    No jogo {i+1}, fez {g} gols.")
        print("-"*40)
print("<< VOLTE SEMPRE >>")