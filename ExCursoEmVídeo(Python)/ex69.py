print("=" * 20)
print(f"{'CADASTRAR PESSOAS':^30}")
print("=" * 20)
mi = mm = h = 0
p = 1
while True:
    i = int(input("Idade: "))
    s = str(input("Sexo [M/F]: ")).strip().upper()[0]
    while s not in 'MmFf':
        s = str(input("Sexo [M/F]: ")).strip().upper()[0]
    print("=" * 20)
    o = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    while o not in 'SsNn':
        o = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if i > 18:
        mi += 1
    if s in "Mm":
        h += 1
    if s in "Ff" and i < 20:
        mm += 1
    if o in "Ss":
        p += 1
    elif o in "Nn":
        break
print(f"Dentro dessas {p} pessoas, {mi} são maiores de 18 anos, {h} são homens e", end='')
print(f" {mm} são mulheres com menos de 20 anos.")
print("\033[1;31mPrograma encerrado!")
