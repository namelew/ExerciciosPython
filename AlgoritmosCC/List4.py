#Ex1
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
#Ex2
h = float(input("Hectares: "))
p = float(input("Preço Tonelada(Soja): R$ "))
t = h * 3
print(f"Serão produzidos {t:.1f} toneladas.", end='')
if t >= 10:
    print(f" O faturamento será de R$ {(t*p):.2f}.", end='')
    print(f" Com um incentivo de R$ {(t*p)*0.05:.2f}.")
else:
    print(f" O faturamento será de R$ {t*p:.2f}. ", end='')
    print("Com um incentivo de R$ 0.")
#Ex3
va = 60
vb = 52
h = 1
while True:
    df = 45 + (vb * h) - (va * h)
    if df <= 0:
        break
    h += 1
print(f"O veículo A alcançará o veículo B em {h} horas!")
# Ex4
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
# ex5
# Não consegui fazer
# ex6
n = int(input("Número: "))
f = n
fa = 1
print(f"{n}! = ", end= '')
while f > 0:
    print(f"{f}", end='')
    print(" x " if f > 1 else " = ", end='')
    fa *= f
    f -= 1
print(f"{fa}")