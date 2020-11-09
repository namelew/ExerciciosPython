n1 = input("Nome: ")
i1 = int(input("Idade: "))
n2 = input("Nome: ")
i2 = int(input("Idade: "))
if i1 > i2:
    print(f"{n1} é mais velho que {n2}.")
elif i2 > i1:
    print(f"{n2} é mais velho que {n1}.")
else:
    print(f"{n1} e {n2} possuem a mesma idade.")

