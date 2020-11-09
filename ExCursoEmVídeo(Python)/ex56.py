m = 0
fm = 0
im = 0
nm = ''
for c in range(1, 5):
    print("-" * 4, "Pessoa", c, "-" * 4)
    n = input("Nome: ")
    i = int(input("Idade: "))
    s = str(input("Sexo(M/F): ")).strip()
    m += i
    if s in "Ff" and i < 20:
        fm += 1
    if s in "Mm" and i > im:
        im = i
        nm = n
print(f"A média de idade do grupo foi {m/4:.2f} anos;")
print(f"O nome do homem mais velho é {nm.strip().capitalize()};")
if fm == 0:
    print("E dentro do grupo não há mulheres com menos de 20 anos.")
else:
    print(f"dentro do grupo há {fm} mulheres com menos de 20 anos.")
