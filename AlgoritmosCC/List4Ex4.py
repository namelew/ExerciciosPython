c = map = mp = ma = maa = si = sp = sa = 0
while True:
    i = int(input("Idade: "))
    if i == 0:
        break
    p = float(input("Peso: "))
    a = float(input("Altura: "))
    si += i
    sp += p
    sa += a
    c += 1
    if c == 1:
        map = mp = p
        ma = maa = a
    else:
        if a > maa:
            maa = a
        if a < ma:
            ma = a
        if p > map:
            map = p
        if p < mp:
            mp = p
print(f"Médias:\nAltura: {sa/c:.2f};\nPeso: {sp/c:.2f};\nIdade: {si/c:.2f}.")
print(f"Maior/Menor Valor:\nMaior Altura: {maa};\nMenor Altura: {ma};\nMaior peso: {map};\nMenor Peso:{mp}.")
