galera = list()
dado = []
tma = tm = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        tma += 1
    else:
        print(f"{p[0]} é menor de idade")
        tm += 1
print(f"No total temos {tma} maiores de idade e {tm} menores de idade")
